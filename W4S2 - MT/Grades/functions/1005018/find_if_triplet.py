def are_all_consecutive(my_list):
    # for list that is less than 2 elements  
    if len(my_list) < 2:
        is_cons = True
        
    #looking through individual element in the list and test for T/F boolean 
    else:
    
        is_cons = (my_list[0] == my_list[1]-1 and my_list[1] == my_list[2]-1)
    
    return is_cons

print(are_all_consecutive([1,2,3]))
print(are_all_consecutive([7,8,9,10]))
print(are_all_consecutive([8]))
print(are_all_consecutive([1,2,2,3]))
print(are_all_consecutive([1,2,4,5]))