"""

myStr = "asdfghj123423456zxcvbnnnnnf"
count = 0
for item in myStr:
    if item.isalpha():
        count += 1

print(count)



myList = range(100)
powerList = [item ** 2 for item in myList]
print(powerList)


mylist = range(200)
result = [item for item in mylist if item %3 == 0 and item %5 == 0]
print(result)



mylist = [1,2,3,4,5,6]
mylist2 = [5,6,7,8,9]
set1 = set(mylist)
set2 = set(mylist2)
print(set1 & set2)



import functools
import operator
myList = [1,2,3,4,5,6]
print("the multiple list is ",end = "")
print(functools.reduce(operator.mul,myList))
print("the concate is",end = "")
print(functools.reduce(operator.add,["audi","ford","bmw"]))



def get_total(user_input):
    total = 0
    for item in user_input:
        if item.isdigit():
            total += int(item)

    return total

print(get_total("12345"))



myList = [1,2,3,4,5,6]
myDict = {item : item**2 for item in myList}
print(myDict)



def sample_fun(a , *b , **c):
    print(a,b,c)
sample_fun(50,3,f=37)

"""

myTuple = "a","b"
mytuple = ("a","b")
print(myTuple == mytuple )
