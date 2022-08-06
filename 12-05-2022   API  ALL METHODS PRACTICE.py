# Library Imports
import json     # This lib used for converting Python objects to JSON objects
from datetime import datetime
import psycopg2 # For connecting to the database
from flask import Flask # To create application object
from flask import request # To read the request details like parameters/request body
from flask_restful import Api
from sqlalchemy import Column, String, Integer, Date, BOOLEAN, and_, or_
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import NullPool
# Disable session pooling from sqlalchemy side use only postgres pool
from flask import jsonify
import os
from datetime import date

# Create the application object using flask framework
app = Flask(__name__)

# Parse the app instance/object to Api Base class to utilise all the services
api = Api(app)

# This a the base class which should have all database table related features
# To work with any database table operations

Base = declarative_base()

# Construct the database URL which will be used for connecting to right database
database_url = "postgresql://postgres:1526@localhost:5432/postgres"

# poolclass=NullPool - Disable sqlalchemy poolling using NullPool
# as by default Postgres has its own pool

# database_url - Constructed url to create engine object which will then
# be used to perform database operations.

# echo - To capture all database events echo set to True which will give more insights about the
# database operations which will eventually help us to understand what's going on while app
# is being using by the end users (customers)
engine = create_engine(database_url, echo=True, poolclass=NullPool)

# Enabling the engine object , get connceted to the database
conn = engine.connect()

# Create session using sessio maker
Session = sessionmaker(bind=engine)

# Create the session object -This is the object being used in the all data base transactions!
session = Session()

class Xl(Base):
    __tablename__ = "xl"
    customerName = Column("customer_name" , String)
    age          = Column("age" , Integer)
    gender       = Column("gender" , String)
    mobNumber    = Column("mob_no" , Integer , primary_key = True)
    model        = Column("model" , String)
    want_To_Take_Test_Ride = Column("want_to_take_test_ride" , BOOLEAN)
    city         = Column("city" , String)
    district     = Column("district" , String)
    state        = Column("state" , String)


    
@app.route("/get_single_record" , methods = ["GET"])
def getSingleRecord():
    try:
        request_name = request.args.get("name")
        result = session.query(Xl).filter(Xl.customerName == request_name).all()
        convert_dict = [item.__dict__ for item in result]
        for item  in convert_dict:
            del item['_sa_instance_state']
        
        return json.dumps(convert_dict)
        session.commit()

    except Exception as err:
        session.rollback()
        print("Error is ----------------------------------->",err)

    finally:
        session.close()





@app.route("/get_all_records" , methods = ["GET"])
def getAllRecords():
    result = session.query(Xl).all()
    for item in result:
        result_1 = [item.__dict__ for item in result]

    for item in result_1:
        del item['_sa_instance_state']
        

    return json.dumps(result_1)








@app.route("/insert_record" , methods = ["POST"])
def insertRecord():
    try:
        request_body = request.get_json(force = True)
        print("request body---------------------->",request_body)
        for item in request_body:
            record = Xl(customerName = item["customer_name"] ,
                        age = item["age"] ,
                        gender = item["gender"] ,
                        mobNumber = item["mob_no"] ,
                        model = item["model"] ,
                        want_To_Take_Test_Ride = item["want_to_take_test_ride"] ,
                        city = item["city"] ,
                        district = item["district"] ,
                        state = item["state"])

            session.add_all([record])
        session.commit()
        return "Record Inserted Succesfully"
        
    except Exception as err:
        session.rollback()
        print("Error is --------------------->",err)
        return "something wrong with your data"
        
    finally:
        session.close()




@app.route("/update_record" , methods = ["PATCH"])
def updateRecord():

    try:
        request_name = request.args.get("name")
        request_model = request.args.get("model")        
        result = session.query(Xl).filter(Xl.customerName == request_name).update({"model" : request_model})
        session.commit()
        return "Record Inserted Successfully"

    except Exception as err:
        session.rollback()
        print("Error is ---------------->",err)
        return "Data Not Updated"

    finally:
        session.close()
    

app.run(debug = False)
