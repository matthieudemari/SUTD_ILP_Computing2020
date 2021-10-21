def are_all_consecutive(my_list):
        
    is_cons = sorted(my_list) == list(range(min(my_list), max(my_list)+1)) 
    return is_cons

print(are_all_consecutive([1,2,3]))
print(are_all_consecutive([7,8,9,10]))
print(are_all_consecutive([8]))
print(are_all_consecutive([1,2,2,3]))
print(are_all_consecutive([1,2,4,5]))