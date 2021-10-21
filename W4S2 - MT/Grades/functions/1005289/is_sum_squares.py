# 1**2 = 1, 2**2 = 4, 3**2 = 9, 4**2 = 16, 5**2 = 25, 6** 36, 7**2 = 49, 8**2 = 64, 9**2 = 81
# 16 is divisable by 4, 36 is divisable by 9, 64 is divisible by 4, 81 is divisible by 9 
# 1**2 = 1, 2**2 = 4, 3**2 = 9, 5**2 = 25, 7**2 = 49
from numpy import sqrt
def is_sum_squares(number):
    is_sq = False
    if number/4 == int(number/4) or number/9 == int(number/9) or number/25 == int(number/25) or number/49 == int(number/49):
        is_sq = True
    elif (number-1)/4 == int((number-1)/4) or (number-1)/9 == int((number-1)/9) or (number-1)/25 == int((number-1)/25) or (number-1)/49 == int((number-1)/49):
        is_sq = True
    return is_sq

print(is_sum_squares(9))
print(is_sum_squares(5))
print(is_sum_squares(50))
print(is_sum_squares(7))