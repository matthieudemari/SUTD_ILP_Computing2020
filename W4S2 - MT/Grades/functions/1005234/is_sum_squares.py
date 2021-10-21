def is_prime(number):
    n=3
    is_p = None
    if number <= 1:
        is_p = False
    elif number == 2:
        is_p = True
    elif number == 3:
        is_p = True
    elif number%2 == 0:
        is_p = False
    else:
        while number >= n:
            if number == n:
                is_p = True
                break
            elif (number%n == 0):
                is_p = False
                break
            elif(number%n != 0):
                n += 1
               
    return is_p