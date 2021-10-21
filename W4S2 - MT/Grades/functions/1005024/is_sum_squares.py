def is_sum_squares(number):
    is_sq = False
    for x in range(number+1):
        for y in range(number+1):
            if x**2 + y**2 == number:
                is_sq = True
           
    
    return is_sq