def is_prime(number):
    is_p = True
    
    if (number == 1):
        is_p = False
    elif (number == 2):
        is_p = True
    else:
        for possible_divisor in range(2, (number//2)):
            if (number%possible_divisor == 0):
                is_p = False
                
    return is_p