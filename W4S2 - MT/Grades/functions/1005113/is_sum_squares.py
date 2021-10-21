def is_sum_squares(number):
    for i in range(int(number**0.5)):
        if ((number - i**2)**0.5 % 1) == 0 :
            return True
    return False

print(is_sum_squares(9))
print(is_sum_squares(5))
print(is_sum_squares(50))
print(is_sum_squares(7))