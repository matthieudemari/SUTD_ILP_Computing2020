def find_if_triplet(my_list):
    count = 0
    curVal = None
    for i in my_list:
        if i == curVal:
            count += 1
            if count == 3:
                return True
        else:
            curVal = i
            count = 1
    return False