def find_if_triplet(my_list):
    has_triplet = None
    tripcounter = 0
    for i in my_list:
        tripcounter += 1
        for j in my_list:
            if(i == j):
                tripcounter += 1
    if(tripcounter  % 3 == 0):
        has_triplet = True
    else:
        has_triplet = False
    return has_triplet