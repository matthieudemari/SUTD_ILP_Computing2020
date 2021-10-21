def is_sum_squares(number):
    
    x = number
    is_sq = False
    
    my_list = []
    
    while x > -1 :
        my_list.append (x)
        x = x - 1
        
    for y in my_list:
        for z in my_list:
            if y**2 + z**2 == number:
                is_sq = True

    return is_sq