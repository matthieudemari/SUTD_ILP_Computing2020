def are_all_consecutive(my_list):
    is_cons = None
    length = len(my_list)
    ff = 0
    if length <= 1:
        is_cons = True
    elif (length > 1):
        while ff <= (length-1):
            if (my_list[ff] != (my_list[ff+1] +1)):
                is_cons = False
                break
            elif (my_list[ff] == (my_list[ff+1] +1)):
                is_cons = True
                ff += 1
                
    return is_cons