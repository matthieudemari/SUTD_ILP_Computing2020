def are_all_consecutive(my_list):
    is_cons = True
    for index, value in enumerate(my_list):
        if(len(my_list) == 1):
            break
            
        if(my_list[index] == my_list[index - 1]):
            is_cons = False
            break
        
    return is_cons