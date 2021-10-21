def are_all_consecutive(my_list):
    if len(my_list) == 0 or len(my_list) == 1:
        is_cons = True
        return is_cons
    else:
        for i in range(1, len(my_list)):
            #print(i-1, i)
            if my_list[i-1] == my_list[i]-1:
                is_cons = True
            else:
                is_cons = False
                break
        return is_cons