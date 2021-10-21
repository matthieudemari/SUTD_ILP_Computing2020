def find_if_triplet(my_list):
    has_triplet = False
    current = 0
    counter = 0
    for i in my_list:
        if i == current:
            counter+=1
        else:
            counter = 0
        if counter == 2:
            has_triplet = True
            break
        current = i
    return has_triplet