def is_prime(number):
    is_p = False
    number_of_divisors = 0
    divisor = 1
    while(divisor <= number):
        if(number % divisor == 0):
            number_of_divisors += 1
        divisor += 1
    if(number_of_divisors == 2):
        is_p = True
    return is_p