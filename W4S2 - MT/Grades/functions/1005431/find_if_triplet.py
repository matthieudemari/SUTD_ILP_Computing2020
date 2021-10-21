def are_all_consecutive(my_list):
    is_cons = (sorted(my_list) == list(range(min(my_list), max(my_list)+1)))
    return is_cons