"""

myStr = "india india india"
myOutput = [item for item in myStr if item == "a"]
join = "".join(myOutput)
count = str(len(join))
print(count)
print(join)
myset = set(join)
print(myset)
final = (count + "".join(myset))
print(final)

#  O/P :-  3a

-------------------------------------------------------------------------------------------

myStr = "india india india"
myList = [item for item in myStr if item == "i" or item == "d" or item == "a"]

myset = set(myList)
join = "".join(myset)
convertList = list(join)
print(join)




myStr = "india india india"
myList = [item for item in myStr if item == "i" or item == "d" or item == "a"]
myList2 = []
output = [myList2.append(item) for item in myList if item not in myList2]
print("".join(myList2[::-1]))

#  O/P :- adi

----------------------------------------------------------------------------------------------------

myStr = "india india india"
myDict = {item : myStr.count(item) for item in myStr if item.isalpha()}
print(myDict)

#  O/P :-  {'i': 6, 'n': 3, 'd': 3, 'a': 3}

------------------------------------------------------------------------------------------------------



myStr = "india india india"
myDict = {item :myStr.count(item) * item for item in myStr if item.isalpha()}
print(myDict)

#  O/P :-  {'i': 'iiiiii', 'n': 'nnn', 'd': 'ddd', 'a': 'aaa'}

#-------------------------------------------------------------------------------------------------------

fruits = ["mango" if i%3==0 else "orange" for i in range(10)]
print(fruits)



myNumList = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

result = [item for item in myNumList]
a = []
result = [item for item in result if item%2 == 0 else item%2 != 0)]
print(a)
print(b)
print(result)

--------------------------------------------------------------------------------------------------


myDict = {1 : "one" , 2 : "two"}
print(myDict.values())

--------------------------------------------------------------------------------------------------

mystr = "ajksdhfjshfdhjfhdf"
print(mystr.count("s "))

-------------------------------------------------------------------------------------------------



number = 20
myrange = range(1,11)
for item in myrange:
    print(number , 'x' , item , '=' , number * item)


-----------------------------------------------------------------------------------------------------



my_dict = {"gfg" : [4, 1, 6], "is" : [1, 4, 8], "best" : [9, 10, 1]}
print(my_dict["gfg"][2])

#  Output : 1

---------------------------------------------------------------------------------------------------


nested_dict = { 'dictA': {'key_1': 'value_1'},'dictB': {'key_2': 'value_2'}}
print(nested_dict["dictA"]["key_1"])    #  value_1
print(nested_dict["dictB"])             #  {'key_2': 'value_2'}
print(nested_dict["dictB"]["key_2"])    #  value_2



print(a["resource"]["location"][0]["location"]["display"])
print(a["resource"]["status"])
print(a["resource"]["subject"]["display"])
print(a["resource"]["period"]["start"])
print(a["resource"]["identifier"][0]["system"])
print(a["resource"]["identifier"][0]["use"])
print(a["resource"]["identifier"][1]["name"])
print(a["resource"]["location"][0]["location"]["reference"])
----------------------------------------------------------------------------------------------------

"""
                
a = {"resource": {"class": {"code": "13","display": "Support OP Encounter",
"system": "urn:oid:1.2.840.114350.1.72.1.7.7.10.696784.13260"},
"id": "ex6x-.onDJ.UfYweCbBoqDg3",
"identifier": [{"system": "urn:oid:1.2.840.114350.1.13.0.1.7.3.698084.8","use": "usual","value": "27560"},{"name":"jai"}],
"location": [{"location": {"display": "EMC Family Medicine","reference": "Location/e4W4rmGe9QzuGm2Dy4NBqVc0KDe6yGld6HW95UuN-Qd03"}}],
"period": {"end": "2019-05-28","start": "2019-05-28"},
"resourceType": "Encounter","status": "in-progress","subject": {"display": "Roberts, Olivia Anne",
"reference": "Patient/eh2xYHuzl9nkSFVvV3osUHg3"},"type": [{"coding": [{"code": "101",
"display": "Office Visit","system": "urn:oid:1.2.840.114350.1.13.0.1.7.10.698084.30"}],
"text": "Office Visit"}]}}


b = {}
##b["display"] = a["resource"]["location"][0]["location"]["display"]
##b["status"] = a["resource"]["status"]

b["identifier"] = a["resource"]["identifier"][0]["value"]
b["period"] = a["resource"]["period"]
b["status"] = a["resource"]["status"]
b["type"] = a["resource"]["type"][0]["coding"][0]["display"]
b["location"] = a["resource"]["location"][0]["location"]["display"]

print(b)

##print(">>>>>>>>>>>>>>>>>>>>>>",a["resource"]["identifier"][0]["value"])
##print(a["resource"]["period"])
##print(a["resource"]["status"])
##print(a["resource"]["type"][0]["coding"][0]["display"])
##print(a["resource"]["location"][0]["location"]["display"])



#   How to get 10th table in python


                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            ##number = 10
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            ##myRange = range(11,21)
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            ##for item in myRange:
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            ##    print(number , "x" , item , "=" , item * number)






























