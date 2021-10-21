def is_prime(number):
    divisors = []
    
    for value in range(1, number+1):  
        if(number % value == 0):
            divisors.append(value)
    
    if len(divisors) == 2:
        is_p=True
        
    else:
        is_p=False
        
    return is_p
    
print(is_prime(1))
print(is_prime(3))
print(is_prime(6))