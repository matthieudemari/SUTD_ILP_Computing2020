def is_sum_squares(number):
    is_sq = False
    first = [value for value in range(100)]
    second = [value for value in range(100)]
    for first_number in first:
        for second_number in second:
            if (first_number ** 2 + second_number ** 2 == number):
                is_sq = True
    return is_sq