def are_all_consecutive(my_list):
    is_cons = None
    min_val = min(my_list)
    max_val = max(my_list)
    if my_list == list(range(min_val, max_val+1)):
        is_cons = True
    else:
        is_cons = False
    return is_cons