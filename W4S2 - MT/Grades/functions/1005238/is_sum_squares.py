def is_sum_squares(number):
    from numpy import sqrt
    is_sq = False
    numberrooted = sqrt(number)
    roundednumberrooted = round(numberrooted)
    if (numberrooted-roundednumberrooted==0.0):
        is_sq = True
#unsure about parts typed below
    elif (numberrooted-roundednumberrooted!=0.0):
        if(number%5==0):
            is_sq = True
        else:
            pass
    return is_sq

print(is_sum_squares(9))
print(is_sum_squares(5))
print(is_sum_squares(50))
print(is_sum_squares(7))