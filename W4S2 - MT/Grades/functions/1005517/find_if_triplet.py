def are_all_consecutive(my_list):
    
    is_cons = False
    new_list = []

    for x in range(my_list[0], (len(my_list))+1):
        
        print(x)
        new_list.append(x)
        if new_list == my_list:
            is_cons = True
     
            

    return is_cons
        