def are_all_consecutive(my_list):
    #take last number in the list - first number in the list
    #if it equals to len(list)-1, it is consecutive
    if (len(my_list)-1) == (my_list[-1]-my_list[0]):
        is_cons = True
    else:
        is_cons = False
    return is_cons