def is_sum_squares(number):
    
    is_sq = False
    
    square = [a**2 for a in range (0,9000,1)]
    
    if number in square:
        is_sq = True

    for b in square:
        number2 = number - b 

        if number2 in square:
            is_sq = True
            break

        else:
            is_sq = False
                
            
    return is_sq