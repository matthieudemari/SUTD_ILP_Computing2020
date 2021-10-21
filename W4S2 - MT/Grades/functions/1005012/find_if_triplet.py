def find_if_triplet(my_list):
    has_triplet = False
    count = 0
    store = my_list[0]
    for i in my_list:
        if i == store:
            count += 1
            if count >= 3:
                has_triplet = True
        elif i != store:
            count = 1
            store = i
    return has_triplet