# Library Imports
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


class Dealer(Base):
    """ Dealer model which has all details -table names & columns"""
    __tablename__ = "dealer"
    dealerName = Column("dealer_name", String)
    dealerCode = Column("dealer_code", String, primary_key = True)
    dealerstate = Column("dealer_state",String)



class Credential(Base):
    __tablename__ = "credential"
    userName = Column("user_name" , String)
    passWord = Column("password" , String , primary_key = True)



@app.route('/getAllRecords' , methods = ['GET'])
def get_all_records():
    req_user_name = request.args.get('username')
    req_password = request.args.get('password')
    req_dealercode = request.args.get('code')

    #req_dealer_code = request.args.get('dealercode')
    try:
        user_result = session.query(Credential).filter(Credential.userName == req_user_name).\
            filter(Credential.passWord == req_password).all()
        #dealer_result = session.query()

    except Exception as err:
        session.rollback()
        print ("err ----> ", err)
        return "error in login page"

    if user_result:
        print("i am inside if --------")
        try:
            dealer_result = session.query(Dealer).filter(Dealer.dealerCode == req_dealercode).all()
        except Exception as err:
            print("error 01 -----> ", err)

    else:
        return "dealer code not found"

    if dealer_result:
        try:
            pe_result = session.query(ProductEnquiry).all()
            convert_dict = [item.__dict__ for item in pe_result]
            for item in convert_dict:
                del item['_sa_instance_state']

            return json.dumps(convert_dict)

        except Exception as err:
            session.rollback()

        finally:
            session.close()

    else:
        return "unauthorized access"





@app.route('/getSingleRecords' , methods = ['GET'])
def get_single_records():
    req_user_name = request.args.get('username')
    req_password = request.args.get('password')
    req_dealercode = request.args.get('code')

    #req_dealer_code = request.args.get('dealercode')
    try:
        user_result = session.query(Credential).filter(Credential.userName == req_user_name).\
            filter(Credential.passWord == req_password).all()
        #dealer_result = session.query()

    except Exception as err:
        session.rollback()
        print ("err ----> ", err)
        return "error in login page"

    if user_result:
        print("i am inside if --------")
        try:
            dealer_result = session.query(Dealer).filter(Dealer.dealerCode == req_dealercode).all()
        except Exception as err:
            print("error 01 -----> ", err)

    else:
        return "dealer code not found"

    if dealer_result:
        try:
            req_existing_vehicle = request.args.get('existingVehicle')
            req_cus_name = request.args.get("name")
            pe_result = session.query(ProductEnquiry).\
                        filter(ProductEnquiry.existingVehicle == req_existing_vehicle and customerName == req_cus_name).all()
            convert_dict = [item.__dict__ for item in pe_result]
            for item in convert_dict:
                del item['_sa_instance_state']

            return json.dumps(convert_dict)

        except Exception as err:
            session.rollback()

        finally:
            session.close()

    else:
        return "unauthorized access"

app.run(debug = False)

app.run(debug = False)
