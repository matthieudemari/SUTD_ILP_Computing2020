def is_sum_squares(number):
    
    first_digit = int(number**0.5)
    #print(first_digit)
    second_digit = int((number-first_digit**2)**0.5)
    #print(second_digit)
    is_sq = number == (first_digit**2 + second_digit**2)
    return is_sq

print(is_sum_squares(9))
print(is_sum_squares(5))
print(is_sum_squares(50))
print(is_sum_squares(7))