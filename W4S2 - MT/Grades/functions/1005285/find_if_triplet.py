def find_if_triplet(my_list):
    has_triplet = False
    i=0
    while i<len(my_list)-2:
        if my_list[i] == my_list[i+1] == my_list[i+2]:
            has_triplet = True
            break
        else:
            i+=1

    return has_triplet