def are_all_consecutive(my_list):
    if (len(my_list) == 1):
        is_cons = True
    else:
        is_cons = True
        for i in range(0, (len(my_list)-1)):
            if (my_list[i] + 1) != (my_list[i+1]):
                is_cons = False
    return is_cons