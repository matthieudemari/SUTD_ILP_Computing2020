def find_if_triplet(my_list):
    has_triplet = False
    # How to count and compare? Use for/enumerate
    # Hint from Prof : 
    # The numbers are sorted, so compare one with those next to it
    for i in my_list:
        if my_list[i] == my_list[i-1] == my_list[i+1]:
            has_triplet = True
            
        else:            
            has_triplet = False
            
    return has_triplet