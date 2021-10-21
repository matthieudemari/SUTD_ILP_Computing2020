def are_all_consecutive(my_list):
    is_cons = True # assume true until proven otherwise
    new_list = my_list[:-1] # new_list has the last element removed to ensure for loop doesnt
                            # call an element in my_list that it beyond the indexed range
    for i, val in enumerate(new_list):
        #print(val, my_list[i+1])
        if(val != my_list[i+1] - 1):
            is_cons = False
            break
    return is_cons