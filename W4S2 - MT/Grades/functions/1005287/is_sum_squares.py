def is_prime(number):
    divisors = []
    for element in range(1, number + 1):
        if number % element == 0:
             divisors.append(element)
                
    print("the divisors are: {}".format(divisors))
    is_p = len(divisors) == 2
    
    return is_p