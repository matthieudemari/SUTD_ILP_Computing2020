def is_sum_squares(number):
    is_sq = False
    for i in range(number):
        for y in range(number):
            if i**2 + y**2 == number:
                is_sq = True
                break
    return is_sq