def are_all_consecutive(my_list):
    is_cons = False
    for i, val in enumerate(my_list):
        if (i > 3):
            val1 = my_list[0]
            val2 = my_list[1]
            val3 = my_list[2]
            val4 = mylist[3]
            is_cons = (val1+3 == val2+2 == val3+1 == val4)
        if (i > 0):
            val1 = my_list[0]
            val2 = my_list[1]
            val3 = my_list[2]
            is_cons = (val1+2 == val2+1 == val3)
        if (i == 0):
            is_cons = True
    return is_cons

print(are_all_consecutive([1,2,3]))
print(are_all_consecutive([7,8,9,10]))
print(are_all_consecutive([8]))
print(are_all_consecutive([1,2,2,3]))
print(are_all_consecutive([1,2,4,5]))