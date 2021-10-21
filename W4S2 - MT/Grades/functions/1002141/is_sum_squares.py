def is_sum_squares(number):
    is_sq = False
    
    for x in range(number+1):
        for y in range(number+1):
            if number == (x)**2 + (y)**2:
                is_sq = True
    
    return is_sq