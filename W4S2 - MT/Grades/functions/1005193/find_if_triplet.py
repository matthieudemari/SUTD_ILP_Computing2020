def are_all_consecutive(my_list):
    is_cons = False
    for i in my_list:
        if my_list.count(i) > 1:
            return is_cons