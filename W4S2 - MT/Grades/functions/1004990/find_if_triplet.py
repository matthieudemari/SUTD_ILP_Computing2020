def find_if_triplet(my_list):
    copy = my_list[:]
    counter = 0 
    has_triplet = False
    for n1 in my_list:
        for n2 in copy:
            if n1==n2:
                counter+=1
        if counter>=3:
            has_triplet = True
        counter=0
    
    return has_triplet