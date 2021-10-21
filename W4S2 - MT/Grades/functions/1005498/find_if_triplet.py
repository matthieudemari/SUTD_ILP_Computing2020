def find_if_triplet(my_list):
    for i in my_list:
        has_triplet = (my_list.count(i) >= 3)
        if has_triplet == True:
            break    
    return has_triplet