def find_if_triplet(my_list):
    count_list = []
    for val in my_list:
        counter = my_list.count(val)
        count_list.append(counter)
    if max(count_list) >= 3:
        has_triplet = True
    else:
        has_triplet = False
    return has_triplet