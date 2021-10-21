def are_all_consecutive(my_list):
    
    if(len(my_list) == 1):
        is_cons = True
    
    else:
        index = 1
        jump = my_list[index] - my_list[index - 1]
        is_cons = jump == 1
    
        while(index <= (len(my_list) - 2)):
            index += 1
            jump = my_list[index] - my_list[index - 1]
            if(jump != 1):
                break
                is_cons = False

    return is_cons