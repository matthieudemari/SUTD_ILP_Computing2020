def is_sum_squares(number):
   
    for a in range(10):
        for b in range(10):
            is_sq = (number == a**2 and b**2)
    return is_sq

print(is_sum_squares(9))
print(is_sum_squares(5))
print(is_sum_squares(50))
print(is_sum_squares(7))