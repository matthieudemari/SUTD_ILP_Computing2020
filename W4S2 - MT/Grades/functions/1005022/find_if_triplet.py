def find_if_triplet(my_list):
    has_triplet = False
    for i in my_list:
        count = 0
        for x in my_list:
            if i == x:
                count += 1
        if count >= 3:
            has_triplet = True
            break
    return has_triplet