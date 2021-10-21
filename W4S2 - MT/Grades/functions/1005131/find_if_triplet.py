def are_all_consecutive(my_list):
    sorted_list = my_list.sort()
    is_cons = sorted_list == my_list
    
    if(sorted_list == my_list):
        is_cons == True
        
    else:
        is_cons == False
        
    return is_cons