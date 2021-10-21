def find_if_triplet(my_list):
    has_triplet = False
    counter_list = [[x,my_list.count(x)] for x in my_list]
    for count in counter_list:
        if count[1] > 2:
            has_triplet = True
            break
    return has_triplet