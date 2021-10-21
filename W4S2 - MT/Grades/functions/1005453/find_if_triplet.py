def find_if_triplet(my_list):

    num_of_times = 1
    for index, value in enumerate(my_list[1:]):
        if value == my_list[index]:
            num_of_times += 1
        else:
            num_of_times = 1
            
        if num_of_times == 3:
            return True
        
    return False