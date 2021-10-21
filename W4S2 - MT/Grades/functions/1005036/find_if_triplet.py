def find_if_triplet(my_list):
    for i in my_list:
        counter = 0
        for j in my_list:
            if i == j:
                counter += 1
            if counter >2:
                return True
    return False