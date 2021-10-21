def find_if_triplet(my_list):
    has_triplet = False
    for number in my_list:
        if my_list.count(number) >= 3:
            has_triplet = True
    return has_triplet