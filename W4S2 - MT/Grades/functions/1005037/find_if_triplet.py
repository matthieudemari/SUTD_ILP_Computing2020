def are_all_consecutive(my_list):  
    i=0
    is_cons = True
    while (i<(len(my_list)-2)):
        if (my_list[i]+1==my_list[i+1]):
            is_cons = True
        else:
            is_cons = False
            break
        i+=1  
    return is_cons