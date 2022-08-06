


myList = ["a123" , "b145" , "c123" , "d123"]
##myDict = {item:item for item in myList if type(item)}
##print(myDict)


my_dict = {}
for item in myList:
    count = 0
    for i in item:
        
        if i.isdigit():
            count += int(i)
    my_dict[item] = count
print(my_dict)

##
##for item in mystr1:
##    if :
##        count += int(item)
##
##        mydict = {item : count for item in myList}
##
##print(mydict)

    

"""

mystr = ""

for item in myList:
    if type(item) == str:
        mystr += item
print(mystr)




myrange = range(1000)

divisible_2_list = []
divisible_7_list = []
divisible_11_list = []


for item in myrange:
    if item%2 == 0:
        divisible_2_list.append(item)


for item in myrange:
    if item%7 == 0:
        divisible_7_list.append(item)


for item in myrange:
    if item%11 == 0:
        divisible_11_list.append(item)  
        
print("divisible by 2 in 6th item is",divisible_2_list[6])
print("divisible by 7 in 6th item is",divisible_7_list[6])
print("divisible by 11 in 6th item is",divisible_11_list[6])

print("divisible by 2 in last second item is",divisible_2_list[-2])
print("divisible by 7 in last second item is",divisible_7_list[-2])






myrange = range(1001)

divisible_by_2_list = []



for item in myrange:
    if item%2 == 0:
        divisible_by_2_list.append(item)

result = len(divisible_by_2_list)//2
print(result)
a = int(input("enter the num :"))
print(divisible_by_2_list[result+a])


def divisible_by_7(userInput):
    div_7 = []
    for item in userInput:
        if item%7 == 0:
            div_7.append(item)

    result = len(div_7)//2
    a = int(input("enter the num :"))
    
    print(div_7[result + a])

userInput = range(int(input("Enter The Range :")))      # range(1000)
divisible_by_7(userInput)




def divisible_by_11(userInput):
    div_by_11 = []
    for item in userInput:
        if item%11 == 0:
            div_by_11.append(item)

    print(div_by_11)
    result = len(div_by_11)//2
    print(result)
    b = int(input("Enter The Number :"))
    print(div_by_11[result + b])

userInput = range(int(input("Enter The Range : ")))
divisible_by_11(userInput)
"""
'''

def divisible_of_2_7_11(userInput):
    divisible_all_num = []
    for item in userInput:
        if item%2 == 0 and item%7 == 0 and item%11 == 0:
            divisible_all_num.append(item)
    print("divisible_all_numbers list is",divisible_all_num)
    all_div_num_length = len(divisible_all_num)//2
    print(all_div_num_length)
    user_number = int(input("Enter The Number : "))
    print(divisible_all_num[all_div_num_length + user_number])

userInput = range(int(input("Enter The Range : ")))
divisible_of_2_7_11(userInput)

'''
















