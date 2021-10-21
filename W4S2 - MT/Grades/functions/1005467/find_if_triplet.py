def find_if_triplet(my_list):
    my_list.sort()
    num_of_elements = len(my_list)
    has_triplet = False
    n = 0
    while (n <= (num_of_elements - 2)
        if my_list[n] != my_list[n+1] or my_list[n+1] != my_list[n+2]
            has_triplet = False
            n +=1
        else (my_list[n] == my_list[n+1] and my_list[n+1] == my_list[n+2])
            has_triplet = True
            
           
    return has_triplet