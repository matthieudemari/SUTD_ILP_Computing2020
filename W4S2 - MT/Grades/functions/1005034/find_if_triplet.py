def find_if_triplet(my_list):
    for i, v in enumerate(my_list):
        if my_list[v] == my_list[v+1] == my_list[v+2]:
            has_triplet = True
            break
        else:
            has_triplet = False
    return has_triplet
