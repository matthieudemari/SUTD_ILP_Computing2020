def is_prime(number):
    is_p = True
    for i in range(2,number-1):
        if number%i == 0:
            is_p = False
            
    if number == 1:
        is_p = False
    
    return is_p

print(is_prime(1))
print(is_prime(3))
print(is_prime(6))