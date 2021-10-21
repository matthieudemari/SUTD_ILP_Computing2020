def are_all_consecutive(my_list):
    is_cons = True
    
    for i, val in enumerate(my_list):
        if (len(my_list)>1):
            if ((i > 0) and (my_list[i]-my_list[i-1] != 1)):
                is_cons = False
            
    return is_cons