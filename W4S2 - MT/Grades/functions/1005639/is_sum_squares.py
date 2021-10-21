def is_sum_squares(number):
    is_sq = False
    for integer_a in range(0, number + 1):
        for integer_b in range(0, number + 1):
            if (number == integer_a**2 + integer_b**2):
                is_sq = True
    return is_sq