def is_prime(number):
    if (number == 1):
        is_p = False
        return is_p
    
    elif (number == 2):
        is_p = True
        return is_p
    
    elif (number % 2 == 0):
        is_p = False
        return is_p
    else:
        is_p = True
    return is_p