def find_if_triplet(my_list):
    has_triplet = False
    n = 0

    if len(my_list) > 3:
        for x in my_list:
            if my_list[n] == my_list[n+1] == my_list[n+2]:
                has_triplet = True
            if n < len(my_list) - 3:
                n += 1
                
    return has_triplet