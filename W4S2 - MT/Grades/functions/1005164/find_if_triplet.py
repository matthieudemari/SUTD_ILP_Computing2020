def are_all_consecutive(my_list):
    is_cons = True
    for i, val in enumerate(my_list):
        if i>0:
            if val == my_list[i-1]+1:
                is_cons = True
            else:
                is_cons = False
                break
    return is_cons