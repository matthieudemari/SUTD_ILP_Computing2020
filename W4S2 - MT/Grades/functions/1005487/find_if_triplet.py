def find_if_triplet(my_list):    
    count = 1
    prev = None
    for ele in my_list:
        if prev == None:
            prev = ele
        else:
            if prev == ele:
                count += 1
                if count == 3:
                    return True
            else:
                count = 1
            prev = ele
    return False