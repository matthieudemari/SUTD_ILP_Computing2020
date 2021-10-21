def are_all_consecutive(my_list):
    is_cons = ()
    new_list = my_list.copy()
    for value1 in new_list:
        for value2 in new_list[new_list.index(value1)::]:
            if (value2-value1 ==1):
                is_cons = True
            elif (len(new_list)==1):
                is_cons = True
            else:
                is_cons = False
    return is_cons
