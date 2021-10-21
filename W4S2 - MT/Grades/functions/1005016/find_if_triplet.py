def find_if_triplet(my_list):
    has_triplet = False
    for x in my_list:
        if(my_list.count(x) >= 3 ):
            has_triplet = True
            break
    return has_triplet