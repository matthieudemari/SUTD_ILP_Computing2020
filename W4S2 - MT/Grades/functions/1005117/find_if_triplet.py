def are_all_consecutive(my_list):
    for index, cur in enumerate(my_list):
        if index != len(my_list)-1:
            if cur + 1 != my_list[index + 1]:
                return False
    is_cons = True
    return is_cons