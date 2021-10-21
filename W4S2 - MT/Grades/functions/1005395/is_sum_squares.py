def is_sum_squares(number):
    is_sq = None
    i = 0
    while (i*i <= number):
        j = 0
        while (j*j <= number):
            if(i*i + j*j == number):
                is_sq = True
            else:
                is_sq = False
def is_sum_squares(number):
    is_sq = None
    i = 0
    while (i*i <= number):
        j = 0
        while (j*j <= number):
            if(i*i + j*j == number):
                is_sq = True
            else:
                is_sq = False
            j = j+1
        i = i+1
    return is_sq