def find_if_triplet(my_list):
    has_triplet = False
    counter = 0
    
    for i in my_list:
        counter = 0
        #print("counter", counter)
        for j in my_list:
            #print(j)
            #print(i)
            #print("------")
            if i == j:
                counter += 1
                #print("counter", counter)
                
            if counter > 2:
                has_triplet = True
                #print("break_")
                return has_triplet
            
    return has_triplet