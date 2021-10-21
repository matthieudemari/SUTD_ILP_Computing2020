def find_if_triplet(my_list):
    
    for val in my_list:
        counter = my_list.count(val)
        
        if counter >= 3:
            has_triplet = True
            break
        
        elif counter < 3:
            has_triplet = False
            counter=0
    
    return has_triplet