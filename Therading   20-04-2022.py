def different_num():
    a = [1,2,3,4,5,6]
    b = [4,5,6,7,8,9]
    diff_num_list = []
    for item in a:
        if item not in b:
            diff_num_list.append(item)

    for item in b:
        if item not in a:
            diff_num_list.append(item)


    return (diff_num_list)

print(different_num())
