def is_sum_squares(number):
    is_sq = False
    if number**0.5 % 1 == 0:
        is_sq = True
    elif number**0.5 % 1 != 0:
        new_num = number / 2
        if new_num**0.5 % 1 == 0:
            is_sq = True
    return is_sq