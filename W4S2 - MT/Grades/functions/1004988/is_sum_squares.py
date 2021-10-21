def is_sum_squares(number):
    for i in range(0,number):
        for j in range(0, number):
            if(i**2 + j**2 == number):
                return True
    return False