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


class Dummy(Base):
    __tablename__ = "dummy"
    name = Column("name" , String)
    age = Column("age" , Integer)
    mobile_no = Column("mobile_no" , Integer ,primary_key = True)
    dummyColumn = Column("dummy_column" , BOOLEAN)


@app.route('/update-records' , methods = ['PATCH'])
def update_records():
    request_name = request.args.get('name')
    result = session.query(Dummy).filter(Dummy.name == request_name).update({"dummyColumn" : False})
    session.commit()


    return "record updated successfully"

app.run(debug = False)




