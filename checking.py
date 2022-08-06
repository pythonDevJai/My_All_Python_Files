"""

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



class Checking(Base):
    __tablename__ = "checking"
    Id = Column("id" , Integer)
    name = Column("name" , String)



@app.route("/get_multi_record" , methods = ["GET"])
def getMultiRecord():
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

"""


a = 12.9
print(int(a))


b = True
print(int(b))


c = np.nan
print(type(c))
