##mystr = "india"
##mydict = {}
##for item in mystr:
##    mydict[item] = mystr.count(item)
##
##print(mydict)
##
##
##dict1 = {1:10,2:20}
##dict2 = {3:30,4:40}
##dict3 = {5:50,6:60}
##newdict = merge(dict1,dict2,dict3)
##print(newdict)
from random import shuffle
"""
def char(a = "asdf1234asdf"):
    alpha = ""
    for item in a:
        if item.isalpha():
            alpha += item

    print(alpha)

char()



def alphaCount(userInput):  
    alpha_count = 0
    int_count = 0
    for item in userInput:
        if item.isalpha():
            alpha_count += 1

        else:
            int_count += 1

    print(alpha_count)
    print(int_count)
userInput = "india123america5678russia"
alphaCount(userInput)
----------------------------------------------------------------------------

mydict = {"a" : 345 , "b" : 4563 , "c" : 435 , "d" : 678}


val = [str(item) for item in mydict.values()]
val2 = []
pfor item in val:
    if item.isdigit():
        val2.append(int(item.replace("3","")))
print(val2)
print(sum(val2))


a = "apple"
b = "apple"
print(a is b)

-----------------------------------------------------------------------------                


mystr = "assssssfnhgfjhffhg"

print(mystr.count("a"))

-----------------------------------------------------------------------------

# Reverse The String

mystr = "hello"
print("".join(reversed(mystr)))
-----------------------------------------------------------------------------


mylist = ["asdf","asdf"]
mystr = "".join(mylist)
print(mystr)

----------------------------------------------------------------------------

mystr = "apple"
print(mystr[0].upper()+ mystr[1:-1] + mystr[-1].upper())

----------------------------------------------------------------------------

l1 = []
for item in range(0,100,2):
    l1.append(item)
print(l1)

---------------------------------------------------------------------------


class Car:
    def __init__(self,color,speed):
        self.color = color
        self.speed = speed

obj = Car("black" , "100kmph")
print(obj.color)
print(obj.speed)

--------------------------------------------------------------------------

mylist = ["world" , "hello"]

print(str("".join(reversed(mylist))))
print(mylist * 2)

-------------------------------------------------------------------------


mystr = "google.com"
mydict = {}
for item in mystr:
    mydict[item] = mystr.count(item)

print(mydict)

------------------------------------------------------------------------


sampleString = 'The lyrics is not that poor'
print(sampleString.replace("not that poor","good"))

------------------------------------------------------------------------


mystr = "aaeeiioouu"
vowel = "aeiou"

print([item for item in mystr if item in vowel])
print(len([item for item in mystr if item in vowel]))

------------------------------------------------------------------------


original_string = "red 12 black 45 green"
print(original_string[0].upper() + original_string[1:-1] + original_string[-1].upper())

----------------------------------------------------------------------------



mylist = [1,2,3,4,5,15,245,240]
print(min(mylist))

---------------------------------------------------------------------------


# Write a Python program to clone or copy a list.

a = [1,2,3,4,5,6]
b = []
for item in a:
    if item not in b:
        b.append(item)

print(b)

------------------------------------------------------------------------------


#  Write a Python program to print a specified list after removing the 0th, 4th and 5th elements.

a = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
b = a[1:4]
print(b)


---------------------------------------------------------------------------------


#  Write a Python program to print the numbers of a specified list after removing even numbers from it.

a = [1,2,3,4,5,6,7,8,9]
b = []
for item in a:
    if item %2 != 0:
        b.append(item)

print(b)

-----------------------------------------------------------------------------------



# Write a Python program to shuffle and print a specified list.

a = [1,2,3,4,5,6,7,8,9]

random.shuffle(a)
print(a)

----------------------------------------------------------------------------------


#  Write a Python program to count the number of elements in a list within a specified range.

myRange = range(1 , 10)
rcount = myRange.count(4)
print(rcount)

----------------------------------------------------------------------------------


# Write a Python program to find common items from two lists.

a = [1,2,3,4,5]
b = [3,4,5,6,7]
c = []
for item in a:
    if item in b:
        c.append(item)

print(c)

---------------------------------------------------------------------------------


# Write a Python program to convert a list of multiple integers into a single integer.

a = [1,2,3,4,5]
#s = str(a)
b = int("".join(map(str,a)))

print(b)
----------------------------------------------------------------------------------


l1 = [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
l2 = []
for item in l1:
    if item not in l2:
        l2.append(item)

print(l2)

-----------------------------------------------------------------------------------

#  Write a Python program to find the items starts with specific character from a given list.

a = ['abcd', 'abc', 'bcd', 'bkie', 'cder', 'cdsw', 'sdfsd', 'dagfa', 'acjd']
userInput = input("Enter The String : ")
empty_list = []
for item in a:
    if item.startswith(userInput):
        empty_list.append(item)

print(empty_list)

----------------------------------------------------------------------------------


# Write a Python program to insert an element at a specified position into a given list.

a = [1, 1, 2, 3, 4, 4, 5, 1]
a.insert(1,10)
print(a)

---------------------------------------------------------------------------------

# Write a Python program to count integer in a given mixed list.

a = [1, 'abcd', 3, 1.2, 4, 'xyz', 5, 'pqr', 7, -5, -12.22]
num_count = 0
for item in a:
    if type(item) == int:
        num_count += 1

print(num_count)

---------------------------------------------------------------------------------


a = "ASDFGasdghsdfWERTYYUIOyuiowert"
b = ""
c = ""
for item in a:
    if item not in b:
        c += item
print(c)

----------------------------------------------------------------------------------


a = [2, 0, 3, 4, 0, 2, 8, 3, 4, 2]
print(a[: :2])

----------------------------------------------------------------------------------
"""
"""
##a = [[12, 18, 23, 25, 45], [7, 12, 18, 24, 28], [1, 5, 8, 12, 15, 16, 18]]
##b = []
##c = []
##for item in a:
##    for item2 in item:
##        if item2 not in b:
##            b.append(item2)
##for item in a:
##    for item2 in item: 
##        if item2 in b:
##            c.append(item2)
##            
##
##    print(item2)
##print(b)



a = [12, 18, 23, 25, 45, 18]
b = []
for item in a:
    if item not in b:
        b.append(item)

print(b)

##a = [{"one": 1} ,{ "one" : 2 },{ "one" : 3}]
##
##d = {}
##for item in a:
##    d["four"] = item
##    
##print(d)


##a = range(10)
##even = []
##for item in a:
##    if item:
##        if item %2 == 0:
##            
##            even.append(item)
##
##print(even)

-------------------------------------------------------------------------
mystr = "hjguyguygy231134yg31ghghgh"
int_str = ""
mydict = {}
for item in mystr:
    if item.isdigit():
        int_str += item
        mydict[item] = mystr.index(item)
print(mydict)
print(int_str)

------------------------------------------------------------------------


def rever(userInput):
    print(userInput[::-1])


userInput = input("Enter The String : ")
rever(userInput)
-----------------------------------------------------------------------


a = [1, 3, 5, 7, 4, 1, 6, 8]
b = []
for item in a:
    if item %2 == 0:
        b.append(item)
        break

for item in a:
    if item %2 != 0:
        b.append(item)
        break

print(tuple(b))

----------------------------------------------------------------------

#  Write a Python program to sort a given mixed list of integers and strings. Numbers must be sorted before strings.

#I/P--> is [19, 'red', 12, 'green', 'blue', 10, 'white', 'green', 1]

#O/P--> Should be --> [1, 10, 12, 19, 'blue', 'green', 'green', 'red', 'white']

a = [19, 'red', 12, 'green', 'blue', 10, 'white', 'green', 1]


int_list = []
str_list = []
for item in a:
    if type(item) == int:
        int_list.append(item)
        int_list.sort()
for item in a:
    if type(item) == str:
        str_list.append(item)
        str_list.sort()

int_list.extend(str_list)
        
print(int_list)

-------------------------------------------------------------------------------------

a = ['4', '12', '45', '7', '0', '100', '200', '-12', '-500']
b = []
for item in a:
    if item.isdigit():
        b.append(int(item))
        b.sort()

print(b)

------------------------------------------------------------------------------------


a = [['Red', 'Maroon', 'Yellow', 'Olive'], ['#FF0000', '#800000', '#FFFF00', '#808000'], ['rgb(255,0,0)', 'rgb(128,0,0)', 'rgb(255,255,0)', 'rgb(128,128,0)']]
a.pop(0)
print(a)

------------------------------------------------------------------------------------


a = [[], [], [], 'Red', 'Green', [1, 2], 'Blue', [], []]
b = []
for item in a:
    if item:
        b.append(item)

print(b)

-------------------------------------------------------------------------------------

a = "qwertyuiasdfghj"
b = "qwertyuicvbnm"
c = ""
for item in a:
    if item not in b:
        c += item

for item in b:
    if item not in a:
        c += item

print(c)
---------------------------------------------------------------------------------------


l1 = [3,4,5]
l2 = [6,7,8]

result = [item+item1 for item,item1 in zip(l1,l2)]

print(result)

-----------------------------------------------------------------------------------------


a = "asdfasdf"
mydict = {}
for item in a:
    mydict[item] = a.count(item)
print(mydict)

-----------------------------------------------------------------------------------------



a = [['orange', 'red'], ['green', 'blue'], ['white', 'black', 'pink']]
a.sort(reverse = True)
print(a)

------------------------------------------------------------------------------------------


myRange = range(200)
result = []
for item in myRange:
    if item%1 == 0 and item%item == 0:
        result.append(int(item))

print(result)

------------------------------------------------------------------------------------------


def dec_fun(num1):
    def wrapper(*args):
        num1 (*args)
        print("whole_num",userInput1 // userInput2)

    return wrapper




@dec_fun
def multi_fun(userInput1,userInput2):
    print("add",userInput1 + userInput2)
    print("multiply",userInput1 * userInput2)
    print("division",userInput1 / userInput2)
    print("modulus",userInput1 % userInput2)


userInput1 = int(input("Enter The Number : "))
userInput2 = int(input("Enter The Number : "))
multi_fun(userInput1,userInput2)


---------------------------------------------------------------------------------------------


#  write a function,To divide the,input into Two Lists.

#  Input = (1,2,3,4)
#  O/P = [1,2]
#        [3,4]


def fun(userInput):
    l1 = []
    l2 = []
    l1.append(userInput[:len(userInput)//2])
    l2.append(userInput[len(userInput)//2:])
    print(l1)
    print(l2)
    
userInput = input("Enter The Value : ")
fun(userInput)

#--------------------------------------------------------------------------------------------



a = [1, 1, 2, 3, 3, 4, 4, 5, 6, 7]
b = [1, 1, 2, 4, 5, 6]
c = []

for item in a:
    if item not in b:
        c.append(item)

print(c)

--------------------------------------------------------------------------------------------


##a = [('V', 60), ('VI', 70), ('VII', 75), ('VIII', 72), ('IX', 78), ('X', 70)]
##b = []
##c = tuple(b)
##
##for item in a:
##    for item2 in item:
##        if type(item2) == int:
##            b.append(item2)
##            b.sort()
##            #c.append(b[0] and b[-1])
##
##print(b[0],b[-1])
###print("--->",c)
##

##
##
##def fun():
##    userInput = (1,2,3,4)
##    l1 = []
##    l2 = []
##    print("------->",len(userInput))
##    #for item in userInput:
##        #if item.isdigit() or item.isalpha():
##    l1.append(userInput[:len(userInput)//2])
##    l2 += (userInput[len(userInput)//2:])
##    print(l1)
##    print(l2)
##    
##
##fun()



def sample(ip1):
    e = []
    for item in ip1:
        if item.isdigit():
            e.append(int(item))
    c = list(e[len(e)//2:])
    d = list(e[:len(e)//2])

    print("c----->", c)
    print("d----->", d)
ip1 = input("enter the number :")
sample(ip1)
---------------------------------------------------------------------------------------------

a = ['0', '1', '2', '3', '4']
b = ['red', 'green', 'black', 'blue', 'white']
c = ['100', '200', '300', '400', '500']
d = [i1+i2+i3 for i1,i2,i3 in zip(a,b,c)]



print(d)
----------------------------------------------------------------------------------------------


mystr = "aasdfghjklasd1234567fghjkl;!@#$%^&*asdfghjkl"
mydict = {}
mydict1 = {}
myalpha = {}
mynum = {}
myspl = {}
result = {}
alphabets = ""
numbers = ""
splchar = ""

for item in mystr:

    mydict[item] = mystr.count(item)
    a = mystr.count(item)
    mydict1[item] = a*item



    if item.isalpha():
        alphabets += item

    elif item.isdigit():
        numbers += item

    else:
        splchar += item

    myalpha["alpha"] = alphabets
    mynum["numbers"] = numbers
    myspl["splchar"] = splchar


    myalpha.update(mynum)
    myalpha.update(myspl)


    result.update(mydict)
    result.update(mydict1)
    result.update(myalpha)


print(mydict)
print("\n",mydict1)
print("\n",myalpha)

print("\n",result)
------------------------------------------------------------------------------------------------


a = [(2, 3), (2, 4), (0, 6), (7, 1)]
b = []
#c = [i2.sort() for item in a for i2 in item]

for item in a:
    for item2 in item:
        b.append(item2)
        b.sort()


print(b[-1],b[-2])
print(type(b))

---------------------------------------------------------------------------------------------------

#   195. Write a Python program to traverse a given list in reverse order, also print the elements with original index.

a = ['red', 'green', 'white', 'black']
b = a[::-1]
for item in b:
    print(a.index(item),item)


--------------------------------------------------------------------------------------------------------


a = ['1', '2', '3', '4', '5', '6', '7' , '8']
b = [i1 + i2 for i1,i2 in zip(a[::2],a[1::2])]
print(b)


-----------------------------------------------------------------------------------------------------------

a = [3, 4, 6, 2, 0, 0, 0, 0, 0, 0, 6, 7, 6, 9, 10, 0, 0, 0, 0, 0, 5, 9, 9, 7, 4, 4, 0, 0, 0, 0, 0, 0, 5, 3, 2, 9, 7, 1]

b = []

for item in a:
    if item == 0:
        b.append(item)

print(b)

--------------------------------------------------------------------------------------------------------------


a = [34.67, 12, -94.89, 'Python', 0, 'C#']
b = []
for item in a:
    if type(item) == int:
        b.append(item)
        
print(b)

-------------------------------------------------------------------------------------------------------------    


a = [1,2,3,4]

mydict = {}

for item in a:
    mydict[item] = item**2

print(mydict)


------------------------------------------------------------------------------------------------------------



a = "google"
b = 0
for item in a:
    if item == "g":
        b += 1
print(b)

------------------------------------------------------------------------------------------------------------


myStr = "india is a beautiful country"
count = 0
for item in myStr:
    if item == " ":
        count += 1

print(count)

-----------------------------------------------------------------------------------------------------------


mystr = "Delete all occurrences of a specified character in a given string"
a = ""
for item in mystr:
    if item != "a":
        a += item

print(a)

--------------------------------------------------------------------------------------------------------


a = [1,2,3,4]
b = [5,6,7,8]
c = [ a + b for (a,b) in zip(a, b)]
print(c)

-------------------------------------------------------------------------------------------------------


myStr = "google"
#O/P = {"g":2 , "o":2 , "l":1 , "e":1}
mydict = {}
for item in myStr:
    mydict[item] = myStr.count(item)
print(mydict)

-------------------------------------------------------------------------------------------------------


userInput = input("enter the string : ")
print(userInput.upper())

-------------------------------------------------------------------------------------------------------


a = "python"
b = a[-2:]
print(b*4)

---------------------------------------------------------------------------------------------------------


a = "1234"
print(a[::-1])

--------------------------------------------------------------------------------------------------------


a = [1,2,3,4,5]
shuffle(a)
print(a)

--------------------------------------------------------------------------------------------------------


a = "asdf"
print(a.startswith("a"))

-------------------------------------------------------------------------------------------------------


import datetime
try:
    a = 10
    print(datetime.datetime.now(),">>>> A is",a,b)

except Exception as err:
    print("Error is",err)

else:
    print("No Error")

finally:
    print("Done")

-------------------------------------------------------------------------------------------------------------


myrange = range(1,20)
count = 0
for item in myrange:
    if item %3 == 0 and item %5 == 0:
        count += 1

print(count)

-------------------------------------------------------------------------------------------------


mylist = [1,2,3,4,5,"abc","india","pvt","Ltd"]
int_count = 0
str_count = 0
for item in mylist:
    if type(item) == int:
        int_count += 1

    else:
        str_count += 1

print("int_count is",int_count)
print("str_count is",str_count)

-------------------------------------------------------------------------------------------------


a = "adadfef!@#$%^&*234123"
b = [item for item in a if not item.isalnum()]
print(b)

-------------------------------------------------------------------------------------------------


def add():
    v1 = int(input("Enter The Value 1 : "))
    v2 = int(input("Enter The Value 2 : "))
print(add())

--------------------------------------------------------------------------------------------------

class python:
    name = "jai" #(This one is Attribute or Variable)
    
    def add(self,a,b): #(This one is Method or Function)
        result = a+b
        print(result)

addition_obj = python() # This is for creating the object.
print(addition_obj.name)
addition_obj.add(10,10) # This one is calling the Funtion with object name. 

-------------------------------------------------------------------------------------------------


mylist = [22.4, 4.0, 16.22, 9.1, 11.0, 12.22, 14.2, 5.2, 17.5]
print(round(min(mylist)))

-------------------------------------------------------------------------------------------------


mystr = "hhjguyguygy231134yg31ghghgh5"
mydict = {}
for item in mystr:
    if item.isdigit():
        mydict[item] = mystr.index(item)
print(mydict)

-------------------------------------------------------------------------------------------------


myList = [[2, 4], [[6, 8], [4, 5, 8]], [10, 12, 14]]
print(len(myList))

-------------------------------------------------------------------------------------------------


mylist = [[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]
summ = max(mylist)
print(sum(summ))

------------------------------------------------------------------------------------------------


myList = [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
second_list = []
for item in myList:
    if item not in second_list:
        second_list.append(item)
print(second_list)

----------------------------------------------------------------------------------------------


str_list = ['abcd', 'abc', 'bcd', 'bkie', 'cder', 'cdsw', 'sdfsd', 'dagfa', 'acjd']
listt = []
userinput = input("enter the charactor : ")
for item in str_list:
    if item.startswith(userinput):
        listt.append(item)
print(listt)


-----------------------------------------------------------------------------------------------




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




# Model for data base table
class ProductEnquiry(Base):
    '''Product enquiry form model which has all details -table names & column'''
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
    isNew = Column("is_new" , BOOLEAN)
    feedBack = Column("feed_back" , String)
    leadStage = Column("lead_stage",String)


class Credential(Base):

    __tablename__ = "credential"
    userName = Column("user_name", String)
    passWord = Column("password", String, primary_key=True)

    
    

@app.route('/cheking' , methods = ['GET'])
def checking_fun():
    request_name = request.args.get('name')
    request_pass = request.args.get('pass')
    authentication = session.query(Credential).filter(Credential.userName == request_name and Credential.passWord == request_pass).all()
    
    if authentication:
        
##        request_email = request.args.get('email')
##        request_occupation = request.args.get('occup')
        result = session.query(ProductEnquiry).all()
##        \
##                 filter(ProductEnquiry.email == request_email and ProductEnquiry.occupation == request_occupation).all()

        convert_dict = [item.__dict__ for item in result]
        for item in convert_dict:
            del item['_sa_instance_state']
        return json.dumps(convert_dict)

app.run(debug = False)


---------------------------------------------------------------------------------------------------------------


##a = {1,2,3,4,5}
##b = {1,2,3,4}
##c = []
##for item in a:
##    if item not in b:
##        c.append(item)
##
##print(set(c))

-----------------------------------------------------------------------------------------------------------------
mystr = "asdf"
print(mystr[::-1])
count = 0
for item in mystr:
    if item:
        count += 1

print(count)

------------------------------------------------------------------------------------------------------------------


mystr = "a-ab-cde-gh2"
print(mystr.reverse())

----------------------------------------------------------------------------------------------------------------------


myList = [1,2,3,4,5,6,7,8,9,10]


print(myList[2::3])


-----------------------------------------------------------------------------------------------------------------
"""

a = 10
b = 10
print(a , "+" , b , "is" ,a + b)
