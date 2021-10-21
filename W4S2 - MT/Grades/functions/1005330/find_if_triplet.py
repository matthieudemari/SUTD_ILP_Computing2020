def are_all_consecutive(my_list):
    is_cons = True
    for index, integer in enumerate(my_list[:len(my_list) - 1]):
        if(integer + 1 == my_list[index + 1]):
            is_cons = True
        else:
            is_cons = False
            break
    return is_cons