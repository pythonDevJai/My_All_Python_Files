##import threading
##import time

"""
a = [1,2,3,4,5,6]
even_num_list = []
def evenNum(a):
    for item in a:
        time.sleep(1)
        if item%2 == 0:
            even_num_list.append(item)
    return even_num_list
print("even_num_list is ",evenNum(a))

odd_num_list = []
def oddNum(a):
    for item in a:
        time.sleep(1)
        if item%2 != 0:
            odd_num_list.append(item)
    return odd_num_list
print("odd_num_list is",oddNum(a))

t1 = time.time()
evenNum(a)
t2 = time.time()
print("even_num_list took time is",t2-t1)


t3 = time.time()
oddNum(a)
t4 = time.time()
print("odd_num_list took time is ", t4-t3)


print("even_num_list & odd_num_list took time is",(t2-t1)+(t4-t3))




mylist = [1,2,3,4,5,6]
even_num_list = []
def evenNum(mylist):
    for item in mylist:
        if item%2 == 0:
            time.sleep(0.5)
            even_num_list.append(item)
    return even_num_list
print(evenNum([1,2,3,4,5,6]))

odd_num_list = []
def oddNum(mylist):
    for item in mylist:
        if item%2 != 0:
            time.sleep(0.5)
            odd_num_list.append(item)
    return odd_num_list
print(oddNum([1,2,3,4,5,6]))


t1 = threading.Thread(target = evenNum , args = ([1,2,3,4,5,6]))
t2 = threading.Thread(target = oddNum , args = ([1,2,3,4,5,6]))

start_time = time.time()

t1.start()
t2.start()

t1.join()
t2.join()

end_time = time.time()

print("total execution time is",end_time - start_time)



"""
##
##my_list = [1,2,3,4,5,6,7,8,9] 
##even_num_list = []
##def evenNum(my_list):
##    for item in my_list:
##        if item%2 == 0:
##            time.sleep(0.5)
##            even_num_list.append(item)
##            
###    return even_num_list
##            print("\n even list is{}".format( even_num_list))
##
##odd_num_list = []
##def oddNum(my_list):
##    for item in my_list:
##        if item%2 != 0:
##            time.sleep(0.5)
##            odd_num_list.append(item)
##                        
###    return odd_num_list
##            print("\n odd list is {}".format(odd_num_list))
##
##
##thread_1 = threading.Thread(target = evenNum, args = ([range(10)]))
##                            
##thread_2 = threading.Thread(target = oddNum, args = ([range(10)]))
##start_time = time.time()
##
##thread_1.start()
##thread_2.start()
##
##thread_1.join()
##thread_2.join()
##
##end_time = time.time()
##
##print("total execution time is {}".format(end_time - start_time))
##
##



def upperCase(userInput):
    upper = ""
    for item in userInput:
        if item.isupper():
            upper += item
    return upper

print(upperCase("ASDGggfhdfDSAFDdsf"))


def upperCase():
    userInput=input("enter input")
    upper = ""
    for item in userInput:
        if item.isupper():
            upper += item
    return upper

print(upperCase())




















            
