"""
#  Count The All Digits Values.


my_list = [1 , 2 , "1" , "2"  , "8wferv" , "5eewfre"]

count = 0
myStr = ""

for item in my_list:
    if type(item) == int:
        count += item


    elif type(item) == str:
        myStr += item

for item in myStr:
    if item.isdigit():
        count += int(item)


print(count)

----------------------------------------------------------------------------------------
#  print the common characters in the given Strings.

myStr1 = "iabkhjm"
myStr2 = "acbmopq"

commonStr = ""

for item in myStr1:
    if item in myStr2:
        commonStr += item

print("Common character is>>>> {}".format(commonStr))


----------------------------------------------------------------------------------------


#  TASK 1

#  print all uppercase characters in one string.
#  print all lowercase characters in one string.



myStr = "DSAdsfdsgfdghDFSFDS"

upperCase = ""
lowerCase = ""

for item in myStr:
    if item.isupper():
        upperCase += item

    elif item.islower():
        lowerCase += item

print("UpperCase char is >>>>> {}".format(upperCase))
print("LowerCase char is >>>>> {}".format(lowerCase))

-----------------------------------------------------------------------------------------------


#   TASK 2

#   check whether the string endswith "y" or Not?
#   Remove all white spaces.
#   Return all uppercase characters.
#   Return all lowercase characters.
   
myStr = "India Is a Beautiful Country"
joinStr = ""
upper_case = ""
lower_case = ""

for item in myStr:
    if item.isalpha():
        joinStr += item

for item in myStr:
    if item.isupper():
        upper_case += item

    elif item.islower():
        lower_case += item
        

print("UpperCase char is >>>>> {}".format(upper_case))
print("LowerCase char is >>>>> {}".format(lower_case))

print("After join my Str is",joinStr)

print("My String Endswith 'y' is",myStr.endswith("y"))


---------------------------------------------------------------------------------------------------


#   TASK 3

# Find the alphabets count & digits count

my_str = "India123AmericA567RussiA"
alphabet_count = 0
digits_count = 0

for item in my_str:
    if item.isalpha():
        alphabet_count += 1

    elif item.isdigit():
        digits_count += 1
        

print("alphabet_count is ",alphabet_count)
print("digits_count is ",digits_count)
        

----------------------------------------------------------------------------------------------------

"""

def checking(userInput):
    for item in userInput:
        if type(item) == str:
            print("True")

        else:
            print("False")

userInput = input("Enter a String : ")
checking(userInput)












