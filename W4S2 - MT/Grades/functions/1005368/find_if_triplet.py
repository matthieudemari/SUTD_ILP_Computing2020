def are_all_consecutive(my_list):
    is_cons = True
    for i in range(len(my_list)-1):
        if my_list[i] != my_list[i+1]-1:
            is_cons = False
    return is_cons

print(are_all_consecutive([1,2,3]))
print(are_all_consecutive([7,8,9,10]))
print(are_all_consecutive([8]))
print(are_all_consecutive([1,2,2,3]))
print(are_all_consecutive([1,2,4,5]))
print(are_all_consecutive([-3,-2,-1,0]))