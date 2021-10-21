def are_all_consecutive(my_list):
    is_cons = False
    for index,value in enumerate(my_list):
        if (my_list[index+1]-value == 1):
            is_cons = True
    return is_cons