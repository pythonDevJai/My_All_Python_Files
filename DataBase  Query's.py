myList = [1,2,3,"india",5,6,7]

def add(input):
    print(sum([item for item in input if type(item) == int]))

add(myList)



mystr = "asdf"
del[mystr]
print("after deleting mystr is",mystr)




myList2 = [item for item in myList if type(item) == str]
print(myList2)



