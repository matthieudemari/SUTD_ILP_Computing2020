def are_all_consecutive(my_list):
    
    consecutive_numbers = 0
    
    for index,number in enumerate(my_list):
        if(my_list[index] - my_list[index-1] == 1):
            consecutive_numbers += 1
    is_cons = consecutive_numbers == (len(my_list)-1)
    return is_cons