def is_prime(number):
    check = 2
    if number == 1:
        is_p = False
        return is_p
    elif number == 2:
        is_p = True
        return is_p
    while number > check:
        if number % check == 0:
            is_p = False
            break
        else:
            check += 1
            is_p = True
    return is_p
