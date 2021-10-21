def is_prime(number):
    is_p = False
    integer_list = []
    i = 0
    while (i <= 99):
        i += 1
        if (number % i == 0):
            integer_list.append(i)
    #return integer_list
    if (len(integer_list) ==2 ):
        is_p = True
    return is_p