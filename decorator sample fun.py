import time


def decorator_func(odd_num):
    def wrapper(args):
        odd_num(args)
        odd_list = []
        st = time.time()
        time.sleep(2)
        for item in args:
            if item%2 != 0:
                odd_list.append(item)
        print(odd_list)
        et = time.time()
        print("execution time is",et-st)
    return wrapper


@decorator_func
def even_num(userInput):
    even_num_list = []
    for item in userInput:
        if item%2 == 0:
            even_num_list.append(item)    
    print(even_num_list)  
    return even_num_list

userInput = range(11)
even_num(userInput)


"""
'''
'''
def decorator_func(odd_num):
    print("i am 3")
    def wrapper(args):
        print("i am 4")
        odd_list = []
        odd_num(args)
        print("i am 5")
##        my_new_list = odd_num(args)
        for item in args:
            if item%2 != 0:
                odd_list.append(item)
        print("i am 6")
        print("odd numbers list is {}".format(odd_list))
    return wrapper




@decorator_func
def even_num(userInput):
    print("i am 1")
    even_num_list = []
    for item in userInput:
        if item%2 == 0:
            even_num_list.append(item)    
    print("Even numbers list is {}".format(even_num_list))  
    print("i am 2")
    return even_num_list

userInput = range(11)
even_num(userInput)








def cube_num(mahesh):
    def  wrapper(args):
        mahesh(args)
        cube_list = [item**3 for item in args]
        print("cube numbers list is {} ".format(cube_list))

    return wrapper

    
@cube_num
def square_num(userInput):
    square_list = [item*item for item in userInput]
    print("square numbers list is {}".format(square_list))
    return square_list

userInput = range(11)
square_num(userInput)    
    
    
"""


































            
