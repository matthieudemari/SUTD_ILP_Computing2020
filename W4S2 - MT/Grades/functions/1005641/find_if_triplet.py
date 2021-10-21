def find_if_triplet(my_list):
    for element in my_list:
        frequency = my_list.count(element)
        if frequency > 2:
            has_triplet = True
        else:
            has_triplet = False
    return has_triplet