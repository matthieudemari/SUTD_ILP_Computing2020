def find_if_triplet(my_list):
    has_triplet = False
    for x in my_list:
        if my_list.count(x)>2:
            has_triplet = True
        else:
            has_triplet = False
            
    return has_triplet