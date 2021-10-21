def is_prime(number):
    is_p = False
    if (number == 1):
        prime1 = number % 1
        is_p = (prime1 == 0)
    else:
        prime = number % number 
        prime1 = (number + 1) % 2
        is_p = (prime == 0 and prime1 == 0)
    return is_p

print(is_prime(1))
print(is_prime(3))
print(is_prime(6))