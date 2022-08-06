"""
                                         #  String Methods

#   Strip

myStr = "             apple              "
print(myStr.lstrip())
print(myStr.rstrip())


#   Split

myStr = "banana"
print(myStr.split("a"))
print(myStr.split("n"))


#   join

myStr = "cherry"
myStr1 = "*".join(myStr)
myStr2 = " ".join(myStr)

print(myStr1)
print(myStr2)


#   Replace

myStr = "cars india"
print(myStr.replace(" ","->"))


#   Lower

myStr = "InDia"
print(myStr.lower())

#   Upper

print(myStr.upper())
"""


                                           #  Listt Methods  
"""
#   Append

myNumList = [1,2,3,4,5]
myNumList.append(6)
print(myNumList)


myCarList = ["AUDI" , "BMW" , "TATA" ]
myCarList.append("SUZUKI")
print(myCarList)


cityList = ["Chennai" , "Mumbai" , "Kolkatta"]
cityList.append("Delhi")
print(cityList)


#   Extend

myNumList = [1,2,3,4,5]
myNumList.extend([6,7,8,9,10])
print(myNumList)


myCarList = ["AUDI" , "BMW" , "TATA" ]
myCarList.extend(["SUZUKI" , "RENAULT" , "HYUNDAI" , "NISSAN"])
print(myCarList)


cityList = ["Chennai" , "Mumbai" , "Kolkatta"]
cityList.extend(["Pune" , "Delhi" , "Bengaluru"])
print(cityList)

"""


if 5>3:
    print("Hi")

a = "12233"
print(int(a))

