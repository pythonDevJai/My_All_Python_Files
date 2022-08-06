# Library Imports
import random
import json     # This lib used for converting Python objects to JSON objects
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




# Model for data base table
class ProductEnquiry(Base):
    """ Product enquiry form model which has all details -table names & columns"""
    __tablename__ = "productenquiry"
    customerName = Column("customer_name", String)
    dealerName = Column("dealer_name" , String)
    createdDate = Column("created_date", String)
    mobileNumber = Column("mob_no", Integer, primary_key=True)
    email = Column("email", String)
    vehicleModel = Column("vehicle_model",String)
    state = Column("state",String)
    district = Column("district",String)
    city = Column("city",String)
    existingVehicle = Column("existing_vehicle",String)
    wantTestDrive = Column("want_to_take_a_test_ride", BOOLEAN)
    dealerState = Column("dealer_state",String)
    dealerTown = Column("dealer_town",String)
    dealerCode = Column("dealer_code" , String)
    briefAboutEnquery = Column("brief_about_enquiry", String)
    expectedDateOfPurchase = Column("expected_date_of_purchase", String)
    intendedUsage = Column("intended_usage", String)
    age = Column("age" , Integer)
    gender = Column("gender" , String)
    occupation = Column("occupation" , String)
    feedBack = Column("feed_back" , String)
    isNew = Column("is_new")



class CustomerProductEnquiry(Base):
    """ Product enquiry form model which has all details -table names & columns"""
    __tablename__ = "customerproductenquiry"
    customerName = Column("customer_name", String)
    dealerName = Column("dealer_name" , String)
    createdDate = Column("created_date", String)
    mobileNumber = Column("mob_no", Integer, primary_key=True)
    email = Column("email", String)
    vehicleModel = Column("vehicle_model",String)
    state = Column("state",String)
    district = Column("district",String)
    city = Column("city",String)
    existingVehicle = Column("existing_vehicle",String)
    wantTestDrive = Column("want_to_take_a_test_ride", BOOLEAN)
    dealerState = Column("dealer_state",String)
    dealerTown = Column("dealer_town",String)
    dealerCode = Column("dealer_code" , String)
    briefAboutEnquery = Column("brief_about_enquiry", String)
    expectedDateOfPurchase = Column("expected_date_of_purchase", String)
    intendedUsage = Column("intended_usage", String)
    age = Column("age" , Integer)
    gender = Column("gender" , String)
    occupation = Column("occupation" , String)
    errorMsg = Column("error" , String)
    isProcessed = Column("is_processed" , BOOLEAN)

    


    
def validate_date(date):

    # initializing string
    test_str = '2022-09-16'
    # initializing format
    format = "%Y-%m-%d"

    # checking if format matches the date
    res = True

    try:
        print(datetime.strptime(test_str, format))
        res = bool(datetime.strptime(test_str, format))
    except ValueError:
        res = False
    finally:
        return res




# POST Service
@app.route('/validate_post_record', methods=['POST'])
def postRecords():
    try:
        request_body = request.get_json(force=True)
        error_msg = ""
        for index, item in enumerate(request_body):
            if type(item["mob_no"]) == int:
                pass

            else:
                item["mob_no"] = random.randrange(10000)
                error_msg += "Enter The Valid Mobile Num"
            record = ProductEnquiry(customerName=item["customer_name"],
                                    mobileNumber=item["mob_no"],
                                    email=item["email"],
                                    vehicleModel=item["vehicle_model"],
                                    errorMsg = error_msg)

            session.add_all([record])
        session.commit()
        return "Records Inserted successfully"
    except Exception as err:
        session.rollback()
        print("error is >>>>>>>>>>>>",err)
        return "data not inserted"
    finally:
        session.close()

app.run(debug = False)

##
##@app.route('/insert_records1', methods=['POST'])
##def inserRecord():
##    try:
##        request_body = request.get_json(force=True)
##        error_msg = ""
##        for item in request_body:
##            if type(item["mobilenumber"])==int:
##                pass
##            else:
##                item["mobilenumber"] = random.Random(10000)
##                error_msg += "Mob num must be of int type "
##            if item["emailid"].endswith(".com"):
##                pass
##            else:
##                error_msg += "Invalid email id"
##            if item["createddate"]:
##                result = validate_date(item["createddate"])
##                if result:
##                    pass
##                else:
##                    error_msg += "Incorrect data format"
##            record = CustomerProductEnquiry(customerName=item["customer_name"],
##                                 mobileNumber=item["mobilenumbe"],
##                                 email=item["email"],
##                                 error=error_msg
##                                 )
##
##            session.add_all([record])
##        session.commit()
##        return "data inserted"
##    except Exception as err:
##        session.rollback()

