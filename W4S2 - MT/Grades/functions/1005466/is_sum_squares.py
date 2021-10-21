def is_prime(number):
    bool1 = (number/1 == number)
    bool2 = (number/number == 1)
    bool3 = (number%(number-2) == 0)
    if(bool1 and bool2 and bool3):
        if(number == 1):
            is_p = False
        else:
            is_p = True
    else:
        is_p = False

    return is_p