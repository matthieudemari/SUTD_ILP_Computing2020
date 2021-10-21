def find_if_triplet(my_list1):
    
    my_list2 = my_list1
    counter = 0
    
    for value1 in my_list1:
        for value2 in my_list2:
            if(value1 == value2):
                counter += 1
                
