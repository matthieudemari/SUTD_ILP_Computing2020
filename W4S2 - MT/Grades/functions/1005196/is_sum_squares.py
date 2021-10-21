def is_prime(number):
    is_p = None
    if(number//number == 1 and number%2 == 0 or number%3 == 0):
        is_p = True
    return is_p

print(is_prime(1))
print(is_prime(2),"prime")
print(is_prime(3),"prime")
print(is_prime(4))
print(is_prime(5),"prime")
print(is_prime(6))
print(is_prime(7),"prime")