def find_if_triplet(my_list):
    has_triplet = False
    for i in range(0,len(my_list)-2):
        if (my_list[i+2]==my_list[i]):
            has_triplet = True
    return has_triplet