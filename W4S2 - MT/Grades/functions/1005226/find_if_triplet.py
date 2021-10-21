def are_all_consecutive(my_list):
    for index , value in enumerate(my_list):
        if len(my_list) == 1:
            is_cons = True
        else:
            is_cons = (value == my_list[index-1] + 1)
    return is_cons