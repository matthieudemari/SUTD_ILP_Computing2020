import math
def is_sum_squares(number):
    i=0
    is_sq = False
    while i**2 <number/2:
        number_copy = number
        x = math.sqrt(number_copy - i**2) 
        if x -int(x) ==0:
            is_sq =True
            break
        else:
            i+=1
    return is_sq