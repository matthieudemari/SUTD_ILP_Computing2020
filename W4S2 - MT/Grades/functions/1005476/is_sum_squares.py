def is_prime(number):
    is_p = True
    if number < 2:
        is_p = False
    else:
        for divisor in range (2, number):
            if number % divisor == 0:
                is_p = False
                break
    return is_p