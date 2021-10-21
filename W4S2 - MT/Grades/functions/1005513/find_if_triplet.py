def find_if_triplet(my_list):
    has_triplet = False
    for value in my_list:
        number_of_occurrences = my_list.count(value)
        if (number_of_occurrences >= 3):
            has_triplet = True
        elif (number_of_occurrences < 3):
            continue
    
    return has_triplet