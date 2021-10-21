def is_prime(number):
    is_p = False
    if number > 1:
        
        for i in range(2, number):
            if(number % i == 0):
                is_p = False
                break
        
        else:
            is_p = True
    
    
        
    return is_p

print(is_prime(1))
print(is_prime(3))
print(is_prime(6))
print(is_prime(97))