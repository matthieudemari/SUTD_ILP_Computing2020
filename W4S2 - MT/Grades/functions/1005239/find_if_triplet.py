def are_all_consecutive(my_list):
    for x in my_list:
        max_value = max(my_list) + 1
        min_value = min(my_list)
        cons_list = list(range(min_value, max_value))
        if (cons_list == my_list):
            is_cons = True
        else:
            is_cons = False
    return is_cons