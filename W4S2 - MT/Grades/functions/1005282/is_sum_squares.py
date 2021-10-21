def is_prime(number):
    is_p = None
    if (number == 1):
        is_p = False
        return is_p
    i = 2
    while i < number:
        remainder = number % i
        if (remainder == 0):
            is_p = False
            return is_p
        i += 1
    is_p = True
    return is_p