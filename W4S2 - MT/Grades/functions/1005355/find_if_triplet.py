def find_if_triplet(my_list):
    for element in my_list:
        for element1 in my_list:
            for element2 in my_list:
                has_triplet = element==element1==element2
    return has_triplet