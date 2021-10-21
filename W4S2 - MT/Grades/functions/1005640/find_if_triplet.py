def are_all_consecutive(my_list):
    is_cons = True
    index = 0 
    
    while index < len(my_list) - 1:
        
        if my_list[index] != my_list[index+1] - 1:
            is_cons = False
            break
        index+=1
    
        
    return is_cons