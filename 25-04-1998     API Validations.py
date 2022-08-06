# Library Imports
import random
from datetime import datetime
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





def validate_customer_name(req_body):
    for item in req_body:
        if type(item['customer_name']) == str:
            return True
        else:
            
            return False


def validate_mob(req_body):
    for item in req_body:
        if type(item['mob_no']) == int:
            str_no = str(item['mob_no'])
            if len(str_no) == 10:
                return True
            else:
                
                return False
##        else:
##            return False


def validate_email(req_body):
    for item in req_body:
        if (item['email']).endswith(".com" or ".in" or ".org"):
            return True
        else:
            
            return False




@app.route('/post_data', methods = ['POST'])
def post_data():
    try:
        error_message = ""
        req_body = request.get_json(force=True)
        for item in req_body:
            

            if validate_customer_name(req_body):
                pass
                print("error_msg ---> ", error_message)
            else:
                error_message += "Customer name is invalid ({}).".format(item['customer_name'])

                

            if validate_mob(req_body):
                pass
            else:
                error_message += " Invalid number format ({}).".format(item['mob_no'])
                


            if validate_email(req_body):
                pass
            else:
                error_message += " Invalid email format ({}).".format(item['email'])
                


            result = CustomerProductEnquiry(customerName=item['customer_name'],
                                            mobileNumber=item['mob_no'],
                                            email=item['email'],
                                            vehicleModel=item['vehicle_model'],
                                            state=item['state'],
                                            district=item['district'],
                                            city=item['city'],
                                            existingVehicle=item['existing_vehicle'],
                                            wantTestDrive=item['want_to_take_a_test_ride'],
                                            briefAboutEnquery=item['brief_about_enquiry'],
                                            expectedDateOfPurchase=item['expected_date_of_purchase'],
                                            gender=item['gender'],
                                            age=item['age'],
                                            occupation=item['occupation'],
                                            intendedUsage=item['intended_usage'],
                                            createdDate=datetime.now(),
                                            dealerCode=item['dealer_code'],
                                            dealerState=item['dealer_state'],
                                            dealerTown=item['dealer_town'],
                                            dealerName = item["dealer_name"],
                                            errorMsg=error_message,
                                            isProcessed=0)

            session.add_all([result])
        session.commit()
        

    except Exception as err:
        print("error ---------> ", err)
        session.rollback()
        return "data not inserted"

    finally:
        session.close()
        return "Record inserted successfully!!"
        

app.run(debug = False)
    
