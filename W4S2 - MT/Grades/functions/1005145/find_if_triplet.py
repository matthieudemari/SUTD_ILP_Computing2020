def are_all_consecutive(my_list):
    for i, v in enumerate (my_list):
        oh = my_list[i]
        my = my_list [i-1]
        if (my>oh):
            is_cons = False
        elif (my<oh):
            is_cons = True
    return is_cons

#Very unsure with lists