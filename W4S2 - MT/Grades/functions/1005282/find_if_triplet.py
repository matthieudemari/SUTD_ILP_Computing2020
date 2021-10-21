def are_all_consecutive(my_list):
    is_cons = None
    if (len(my_list) == 1):
        is_cons = True
    else:
        for i in range(len(my_list)-1):
            bool1 = ((my_list[i+1] - my_list[i]) == 1)
            if (bool1 == False):
                is_cons = False
                return is_cons
        is_cons = True
    return is_cons