def is_sum_squares(number):
    for a in range(0,number):
        for b in range(0,number): 
            if(((a**2)+(b**2))==number):
                is_sq=True
            else:
                is_sq=False
    return is_sq