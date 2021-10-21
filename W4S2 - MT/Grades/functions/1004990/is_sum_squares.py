def is_sum_squares(number):
    is_sq=False
    for x in range(number):
        for y in range(number):
            if x**2 + y**2 == number:
                is_sq=True
    
    return is_sq