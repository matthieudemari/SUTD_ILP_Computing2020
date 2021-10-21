def is_prime(number):
    is_p = True
    if (number <= 1):
        is_p = False
    elif(number >3 ):
        for i in range(2,number):
            if (number%2 == 0) or (number%3 == 0):
                is_p = False
            else:
                is_p = True
    return is_p