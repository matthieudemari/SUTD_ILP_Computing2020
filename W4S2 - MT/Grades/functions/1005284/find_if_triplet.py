def find_if_triplet(my_list):
    consec=0
    nums= len(my_list)

    for x in range(nums):
        if x + 1    > nums-1:
            break
            
        if my_list[x] == my_list[x+1]:
            consec += 1
        else:
            consec = 0
            
        if consec == 2:
            has_triplet = True
            break
        else:
            has_triplet = False
    
    return has_triplet