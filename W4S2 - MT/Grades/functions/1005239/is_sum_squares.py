def is_prime(number):
    if (number == 1):
        is_p = False
    elif (number > 1):
        for div in range(2, number): 
            number_div = number % div
            if (number_div == 0):
                is_p = False
            else:
                is_p = True
    return is_p