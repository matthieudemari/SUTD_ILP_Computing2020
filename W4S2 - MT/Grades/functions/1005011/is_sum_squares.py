def is_sum_squares(number):
    limiter = int(number**0.5) + 1
    is_sq = False
    for value1 in range(limiter):
        for value2 in range (limiter):
            if (value1**2 + value2**2 == number):
                is_sq = True
                return is_sq
    return is_sq