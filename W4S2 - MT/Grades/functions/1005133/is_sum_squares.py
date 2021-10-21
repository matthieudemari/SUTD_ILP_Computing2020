def is_prime(number):
    is_p = True
    if(number == 1): # hard coded special case for number == 1
        is_p = False
        return is_p
    for i in range(2, number): # if there exists a divisor which has gives no remainder
                               # number is not prime
        if(number % i == 0):
            is_p = False
            return is_p
    return is_p