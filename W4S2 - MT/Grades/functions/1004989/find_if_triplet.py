def find_if_triplet(my_list):
    has_triplet = False
    for number in my_list:
        counter=my_list.count(number)
        if counter>2:
            has_triplet=True
    return has_triplet