def is_sum_squares(number):
    if (number % 2 == 0):
        is_sq = True
    else: 
        is_sq = False
    return is_sq

print(is_sum_squares(9))
print(is_sum_squares(5))
print(is_sum_squares(50))
print(is_sum_squares(7))