def is_sum_squares(number):
    is_sq = None
    i = 0
    while (i < number):
        new_number = number - i**2
        sqrt_new_number = new_number**(0.5)
        if (sqrt_new_number) != round(sqrt_new_number)
            is_sq = False
            i +=1
        else
            is_sq = True
            break
            
    return is_sq