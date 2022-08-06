                                          #  LISTS, TUPLES AND DICTIONARIES

 

1. What is a list?

A list is an ordered set of values, where each value is identified by an index.
The values that make up a list are called its elements. Lists are similar to strings,
which are ordered sets of characters, except that the elements of a list can have any type.

-----------------------------------------------------
 
# create tuple with single element.

myTuple = ("one")
print(type(myTuple))
 
--------------------------------------------------------


4. Mention any 5 list methods.

append() ,extend () ,sort(), pop(),index(),insert and remove()

------------------------------------------------------------------ 

5. State the difference between lists and dictionary.

List is a mutable type meaning that it can be modified whereas dictionary is immutable and is a key value store.
Dictionary is not ordered and it requires that the keys are hashable whereas list can store a sequence of objects in a certain order.

------------------------------------------------------------------------- 

6. What is List mutability in Python? Give an example.

Python represents all its data as objects. Some of these objects like lists and dictionaries are mutable,
i.e., their content can be changed without changing their identity. Other objects like integers, floats, strings and tuples
are objects that cannot be changed.

Example:

>>>     numbers = [17, 123]

>>>     numbers[1] = 5

>>>     print numbers [17, 5]

 

--------------------------------------------------------------------
 


 

10. Write a program in Python to delete first element from a list.

def deleteHead(list): del list[0]

Here’s how deleteHead is used:

>>>     numbers = [1, 2, 3]

>>>     deleteHead(numbers)

>>>     print numbers [2, 3]




---------------------------------------------------------------------



13. Define key-value pairs.

The elements of a dictionary appear in a comma-separated list. Each entry contains an index and a value separated by a colon.
In a dictionary, the indices are called keys, so the elements are called key-value pairs.


-----------------------------------------------------------------------------
 

14. Define dictionary with an example.

A dictionary is an associative array (also known as hashes). Any key of the dictionary is associated (or mapped) to a value.
The values of a dictionary can be any Python data type. So dictionaries are unordered key-value-pairs.

Example:

>>> emptyDict = {}  # empty dictionary

>>>     eng2sp['one'] = 1

>>>     eng2sp['two'] = 2

print(emptyDict)

 
----------------------------------------------------------------------------------


# Difference between pop and remove in list?

pop - Removes the element at the specified position,it means index position.

myList = [1,2,3,4,5,6]
myList.pop(0)
print(myList)

remove - Removes the item with the specified value

myList = [1,2,3,4,5,6]
myList.remove(4)
print(myList)

# TypeError: list.remove() takes exactly one argument (0 given)

---------------------------------------------------------------------------------------

#  What will be the output of the given code?
myList=[‘p’,’r’,’i’,’n’,’t’,]
print(myList)

# syntax Error >> because here we should give correct quotaion,like ' / "".


---------------------------------------------------------------------------------------


#  How are the values in a tuple accessed?

myTuple = (1,2,3,4,5,6,7)
print(myTuple[0])


----------------------------------------------------------------------------------------


#  how can you access elements from the dictionary?

myDict = {1 : "one" , 2 : "two" , 3 : "three"}
print(myDict[2])

--------------------------------------------------------------------------------------

#  how can you insert values in to dictionary?


myDict = {1 : "one" , 2 : "two" , 3 : "three"}
myDict[4] = "four"
print(myDict)


-------------------------------------------------------------------------------------

#  Write a Python program access the index of a list.


myList = [1,2,3,4,5,6]
indexList = myList.index[2]
print(indexList)


--------------------------------------------------------------------------------------

#  How to create nesting of tuples ?  

tuple1 = (0, 1, 2, 3)
tuple2 = ('python', 'interviewer')
nested_tuple = (tuple1, tuple2)
print(nested_tuple)


-------------------------------------------------------------------------------------

#  What is difference between Tuple and List ?


-------------------------------------------------------------------------------------

#  How To Concatenate or Join two Lists in Python ?

-------------------------------------------------------------------------------------

#  What is the difference between the list and Tuple ?

The main difference between list and tuple is that Lists are mutable and Tuples are immutable.
In other words, we can make changes(modify) in the list once we declare the list but We cannot do the same in tuples(cannot modify).

List Example:

carList = ["audi","tata","renault"]
carList[3] = "bmw"
print(carList)


Tuple Example:

carTuple = ("audi","tata","renault")
carTuple[1] = "suzuki"
print(carTuple)

# TypeError: 'tuple' object does not support item assignment


----------------------------------------------------------------------------------------

#  How to access dictionary keys only ?































