"""

mystr = "HHjj23aegfdyfsayyyt    GYgygYEDWFG!!@#$%^&1234567ASDFGHJKasdfghj@#"
upperCase = 0
lowerCase = 0
integers = 0
splChar = 0


for item in mystr:
    if item.isupper():
        upperCase += 1

    elif item.islower():
        lowerCase += 1

    elif item.isdigit():
        integers += 1

    else:
        splChar += 1
        

print("upper count is {}".format(upperCase) ,";lower count is {}".format(lowerCase) ,\
      ";integer count is {}".format(integers) , ";splChar count is {}".format(splChar))



# 1. Write a Python program to sum all the items in a list.

myList = [1,2,3,4,5,6,7,8]
print(sum(myList))

"""

# 2. Write a Python program to multiply all the items in a list


myList = [1,2,3,4,5,6,7,8]
print(myList*)
