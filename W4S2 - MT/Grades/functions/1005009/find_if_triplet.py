def are_all_consecutive(my_list):

    if (len(my_list)-1) == (my_list[-1]-my_list[0]):
        is_cons = True
    else:
        is_cons = False
    return is_cons