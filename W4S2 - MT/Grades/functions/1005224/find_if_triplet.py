def find_if_triplet(my_list):
    counter = 1
    has_triplet = None
    for i in my_list:
        while(my_list[i] == my_list[i+1]):
            counter += 1
        return counter
    if(counter >= 3):    
        has_triplet = True
    else:
        has_triplet = False
    return has_triplet