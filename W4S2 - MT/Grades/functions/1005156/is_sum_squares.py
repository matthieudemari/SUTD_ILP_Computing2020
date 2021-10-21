def is_prime(number):
    is_p = ()
    divisors = []
    for value in range(1, number):
        if(number % value == 0):
            divisors.append(value)
    divisors.append(number)
    if (len(divisors)>2):
        is_p = False
    else:
        is_p = True
    print (divisors)
    
    return is_p

print(is_prime(16))
print(is_prime(13))
print(is_prime(61))