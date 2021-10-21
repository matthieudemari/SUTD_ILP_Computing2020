# This does not work :(
def is_sum_squares(number):
 # number is the sum of 0(+n) and number(-n)
    small_number = 0
    large_number = number
    while((small_number == large_number) or (small_number + 1 == large_number)):
            small_number += 1
            large_nnumber -= 1
            is_sq = ((small_number ** 0.5 == int(small_number ** 0.5) and (large_number ** 0.5 == int(large_number ** 0.5))
            if(is_sq == True):
                break
    return is_sq