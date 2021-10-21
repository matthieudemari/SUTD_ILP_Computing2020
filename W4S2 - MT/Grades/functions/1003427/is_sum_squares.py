def is_sum_squares(number):
    is_sq = False
    for first in range(1,int(number**0.5+1)):
            if (number-first**2)**0.5%1==0:
                is_sq = True
                break
    return is_sq