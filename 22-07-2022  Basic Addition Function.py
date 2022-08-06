import time
"""
def add(input1,input2):
    if type(input1) == int and type(input2) == int:
        print(input1 + input2)

            
    else:
            
        if type(input1) != int:
            print("Invalid Input1 Please Enter valid input")

        if type(input2) != int:
            print("Invalid Input2 Please Enter valid input")



add(10,34)

#---------------------------------------------------------------------------------------------

myList = [1,2,3,4,"asdf" , 5,6,"zxcv"]
startTime = time.time()
result = [item for item in myList if type(item) == str]
print(result)
endTime = time.time()
print(endTime - startTime)

#-----------------------------------------------------------------------------------------------

myList = [1,2,3,4,"asdf" , 5,6,"zxcv"]
str_list = []
startTime = time.time()
time.sleep(0.5)
for item in myList:
    if type(item) == str:
        str_list.append(item)
time.sleep(0.5)

print(str_list)

endTime = time.time()
print(endTime - startTime)


#-------------------------------------------------------------------------------------------------
"""

#                                  Constructor Method/Function
start_time = time.time()

class myDetails:
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender

    def get_my_name(self):
        print("my Name Is {}".format(self.name))

    def get_my_age(self):
        print("my age Is {}".format(self.age))

    def get_my_gender(self):
        print("my gender Is {}".format(self.gender))

        
my_obj = myDetails("Jai" , 24 , "Male")

my_obj.get_my_name()
my_obj.get_my_age()
my_obj.get_my_gender()

end_time = time.time()

print(end_time - start_time)




        
