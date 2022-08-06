
def find_odd_num(odd_num):
    def wrapper(args):
        odd_num_list = []
        my_odd_list = odd_num(args)

        for item in my_odd_list:
            if item %2 != 0:
               odd_num_list.append(item)

        print("odd_num_list  is {}".format(my_odd_list))

    return wrapper



@find_odd_num
def find_even_num(userInput):
    even_num_list = []
    for item in userInput:
        if item %2 == 0:
            even_num_list.append(item)

    print("even_num_list  is {}".format(even_num_list))

userInput = range(50)
find_even_num(userInput)

            
