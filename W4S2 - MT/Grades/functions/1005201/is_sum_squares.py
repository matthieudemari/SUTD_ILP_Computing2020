def is_prime(number):
    is_p = None
    if(number == 1):
        is_p = False
    elif(number == 2):
        is_p = True
    elif(number > 2):
        for multiple in range(2,number):
            if (number % multiple) == 0:
                is_p = False
                break
            else:
                is_p = True
    return is_p