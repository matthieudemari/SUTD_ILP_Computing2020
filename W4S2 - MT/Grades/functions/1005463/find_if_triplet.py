def are_all_consecutive(my_list):
    
    #max - min +1 =n --> n is the number of elements in list
    length = len(my_list)
    n = max(my_list)-min(my_list)+1
    
    if (length == n):
        is_cons = True 
        
    else:
        is_cons = False

    return is_cons