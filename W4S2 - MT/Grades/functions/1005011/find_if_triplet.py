def find_if_triplet(my_list):
    has_triplet = False
    for index, value in enumerate(my_list[:-2]):
        if(value == my_list[index + 1] == my_list[index + 2]):
            has_triplet = True
            break
    return has_triplet