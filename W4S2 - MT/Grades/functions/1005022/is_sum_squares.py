def is_sum_squares(number):
    is_sq = False
    for x in range(number):
        for y in range(number):
            if (x**2 + y**2) == number:
                is_sq = True
                break
            elif (x**2 + y**2) > number:
                break
        if is_sq:
            break
    return is_sq