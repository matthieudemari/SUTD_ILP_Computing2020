def is_prime(number):
    list_of_divisors = range(1,number + 1)
    number_of_divisors = 0
    for divisor in list_of_divisors:
        if(number % divisor == 0):
            number_of_divisors += 1
            
    if(number_of_divisors == 2):
        is_p = True
        
    else:
        is_p = False
        
    return is_p