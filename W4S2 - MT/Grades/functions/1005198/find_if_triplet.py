def find_if_triplet(my_list):
    test1 = []
    test2 = []
    for elem in my_list:
        if elem in test1:
            return True
        else:
            test1.extend(elem)  
            for elem in test1:
                if elem in test2:
                    return True
                else:
                    test2.extend(elem)       
    return False
