def is_prime(number):
    
    possible_divisors = []
    
    for divisor in range(1, number+1):
        if (number % divisor == 0):
            possible_divisors.append(divisor)
    
    is_p = len(possible_divisors) == 2 
    return is_p