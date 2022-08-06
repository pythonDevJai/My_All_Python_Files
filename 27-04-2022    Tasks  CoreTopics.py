#******************************************************python core topics

#   1. Data Types
#   2. Operators
#   3. Statements
#       Conditional Statements
#       Control Statements
#   4. Functions
#   5. OOPs
#   6. Types Inheritance

##        Single Inheritance
##        Multiple Inheritance
##        Multiple Inheritance
##        Hierarchical Inheritance
##        Hybrid Inheritance

#   7. Decorators
#   8. Threading
#   9. Multiprocessing
#   10.Exceptional/Error Handling
#   11.Python Memory spaces
#   12.Logging
#   13.Comprehensions
#   14.
"""

mylist = [1,2,3,"abc" , "abcd" , "abcde"]
emptylist = []
for item in mylist:
    if type(item) == str and len(item)>3:
        emptylist.append(item)

print(emptylist)

------------------------------------------
numlist = [1,2,3,4,5,6,7,8,9]
numlist2 = [10,20,30]
for item in numlist:
    for item2 in numlist2:
        print(item,item2)

----------------------------------------
def mahesh(a = 10):
    print("zxcvdf")
mahesh(a=20)

------------------------------------------------------


def addition(userInput):
    input1 = input("enter the num1 :")
    input2 = input("enter the num2 : ")

    if input1.isdigit() and input2.isdigit():
        return int(input1) + int(input2)
    else:
        return "incorrect input : "
userInput = 32
print("Total count is",addition(userInput))

----------------------------------------------------------
"""

def sumfun(userInput):
    print(sum([item for item in userInput if type(item) == int]))

userInput = 1,2,3,"hjgd"
sumfun(userInput)
