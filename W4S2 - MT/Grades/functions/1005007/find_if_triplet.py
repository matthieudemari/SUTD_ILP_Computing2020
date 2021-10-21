def find_if_triplet(my_list):
    has_triplet = False
    
    for i in my_list:
        new_list = my_list
        new_list.remove (i)
        
        for x in new_list:
            if i == x:
                new_list.remove (x)
                
                for y in new_list:
                    if x == y:
                        has_triplet = True
                        
                    
    
    return has_triplet