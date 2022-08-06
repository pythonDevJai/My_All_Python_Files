"""

if 8>3:
    print("INDIA")

if 4<3:
    print("AUS")

if 9<3:
    print("EU")

else:
    print("USA")
-------------------------------------------------------------

import time

myNumList = [1,2,3,4,5,6,7,8]
if 5 in myNumList:
    print(myNumList[4])

else:
    print(0)

----------------------------------------------------------------

myRange = range(100000)
for item in myRange:
    if item %3 == 0 and item %5 == 0:
        time.sleep(1)
        print(item)

------------------------------------------------------------

myRange = range(500)
for item in myRange:
    if item %2 == 0:
        print("Even_list",item)

    else:
        print("Odd_list",item)

---------------------------------------------------------------


myNumList = [1,2,3,4,5,6,7,8]
for item in myNumList:
    print(myNumList)

myTuple = (1 , 2 , "india" , {5,6} , {1:100})
for item in myTuple:
    print(item)


myStr = "I Am Good Boy"
for item in myStr:
    print(item)


mySet = {3 , 4 , "Audi" , (1,2)} # Set can be stored in only immutable Data type. 
for item in mySet:               # Error program i was given in below.
    print(mySet)

myset = {1,2,"asdf" , [5,6] , (3,4) , {"car" : "Audi" }}
print("myset is --------------------------->",myset)

--------------------------------------------------------------------------------
"""



