def is_sum_squares(number):
    is_sq = False
    for i1 in range(number):
        for i2 in range(number):
            if i1**2 + i2**2 == number:
                is_sq = True
                break 
    return is_sq