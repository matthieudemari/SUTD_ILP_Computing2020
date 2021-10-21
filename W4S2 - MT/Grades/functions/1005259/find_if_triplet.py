def are_all_consecutive(my_list):
    i = my_list[0]-1
    for values in my_list:
        if(values == i+1):
            is_cons = True
            i=values
        else:
            is_cons = False
            break
    return is_cons

print(are_all_consecutive([1,2,3]))
print(are_all_consecutive([7,8,9,10]))
print(are_all_consecutive([8]))
print(are_all_consecutive([1,2,2,3]))
print(are_all_consecutive([1,2,4,5]))