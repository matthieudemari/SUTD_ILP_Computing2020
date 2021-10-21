def is_prime(number):
    for i in range(number):
        x = len([i for i in range(1, number+1) if not number % i])
    is_p = x <= 2 and x != 1
    return is_p

print(is_prime(1))
print(is_prime(3))
print(is_prime(6))