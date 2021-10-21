def find_if_triplet(my_list):
    for x in my_list:
        if my_list.count(x) < 3:
            return False
        else:
            return True