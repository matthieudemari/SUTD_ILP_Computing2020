def are_all_consecutive(my_list):
    
    for i, v in enumerate(my_list):
        if (v - my_list[i-1] == 1 and v - my_list[i-2] == 2):
            is_cons = True
        elif(len(my_list) <= 1):
            is_cons = True
        else:
            is_cons = False
   
    return is_cons