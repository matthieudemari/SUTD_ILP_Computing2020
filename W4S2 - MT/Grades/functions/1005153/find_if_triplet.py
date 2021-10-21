def are_all_consecutive(my_list):
    for i,num in enumerate(my_list[:-1]):
        if my_list[i+1] - num != 1:
            return False
    else:
        return True