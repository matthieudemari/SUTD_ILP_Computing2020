def is_prime(number):
    
    
    #checking if the number is odd number and ignore number 1 because its only one divisor
    if (number%2 == 1 and number>1):
        is_p = True
    else:
        is_p = False
        
    return is_p

print(is_prime(1))
print(is_prime(3))
print(is_prime(6))