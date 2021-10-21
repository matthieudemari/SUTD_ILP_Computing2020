def find_if_triplet(my_list):
    test_value=my_list[0]
    counter=0
    has_triplet=False
    for element in my_list:
        if test_value==element:
            counter+=1
            has_triplet = counter>=3
            if has_triplet:
                return has_triplet
                
            
        elif test_value!=element:
            test_value=element
            counter=1
    return has_triplet