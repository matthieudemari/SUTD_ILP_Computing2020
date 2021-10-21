def is_prime(number):
    is_p = True
    integer = 2
    if number > 1:
        while(integer<number):
            if (number%integer == 0):
                is_p = False
            integer+=1
    else:
        is_p = False
    return is_p