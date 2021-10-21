def are_all_consecutive(my_list):
    if len(set(my_list)) == len(my_list) and max(my_list) - min(my_list) == len(my_list) - 1:
        is_cons = True
    else:
        is_cons = False
    return is_cons

print(are_all_consecutive([1,2,3]))
print(are_all_consecutive([7,8,9,10]))
print(are_all_consecutive([8]))
print(are_all_consecutive([1,2,2,3]))
print(are_all_consecutive([1,2,4,5]))