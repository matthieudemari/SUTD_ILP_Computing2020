def find_if_triplet(my_list):
    has_triplet = False
    
    for i in my_list:
        counter = my_list.count(i)
        if counter >= 3:
            has_triplet = True
    
    return has_triplet