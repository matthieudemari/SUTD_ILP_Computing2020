def are_all_consecutive(my_list):
    min_val = min(my_list)
    max_val = max(my_list)
    if my_list == list(range(min_val,(max_val+1))):
        return True
    else:
        return False