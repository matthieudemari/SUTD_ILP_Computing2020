def are_all_consecutive(my_list):
    is_cons = True
    for i,v in enumerate(my_list):
        if i == len(my_list)-1:
            return is_cons
        elif v+1 != my_list[i+1]:
            is_cons = False

print(are_all_consecutive([1,2,3]))
print(are_all_consecutive([7,8,9,10]))
print(are_all_consecutive([8]))
print(are_all_consecutive([1,2,2,3]))
print(are_all_consecutive([1,2,4,5]))