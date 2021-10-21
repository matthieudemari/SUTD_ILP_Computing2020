def is_sum_squares(number):
    is_sq = True
    x_list = list(range(0,9))
    y_list = list(range(0,9))
    for x in x_list:
        for y in y_list:
            if x**2+y**2 == number:
                return is_sq
    
print(is_sum_squares(9))
print(is_sum_squares(5))
print(is_sum_squares(50))
print(is_sum_squares(7))