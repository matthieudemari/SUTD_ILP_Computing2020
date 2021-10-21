def is_sum_squares(number):
    
    is_sq = False
    
    if number <= 0:
        print("try with a number > 0")
    else: 
        for i in range(1000):
            for i2 in range(1000):
                if (i**2 + i2**2 == number):
                    is_sq = True
                    break
                
    return is_sq