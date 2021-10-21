def is_sum_squares(number):
    for a in range(0, number):
        for b in range(0, number):
            if a**2 + b**2 == number:
                return True
    return False