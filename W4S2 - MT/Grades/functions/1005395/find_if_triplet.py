def find_if_triplet(my_list):
    has_triple = None
    i = 0
    j = i+1
    k = j+1
    for i in my_list:
        for j in my_list:
            for k in my_list:
                if (my_list[i] == my_list[j] == my_list[k]):
                    has_triple = True
                else:
                    has_triple = False
                k = k+1
            j = j+1
        i = i+1
            
    return has_triple
