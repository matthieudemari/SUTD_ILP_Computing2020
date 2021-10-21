def find_if_triplet(my_list):
    for value in my_list:
        if my_list.count(value) < 3:
            has_triplet = False
        else:
            has_triplet = True
    return has_triplet