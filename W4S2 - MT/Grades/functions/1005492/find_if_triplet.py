def find_if_triplet(my_list):
    if max(my_list)-min(my_list)<2:
        has_triplet = True
    if max(my_list)-min(my_list)==2:
        has_triplet = True
    elif max(my_list)-min(my_list)>2:
        has_triplet = False
    
        
        
    return(has_triplet)