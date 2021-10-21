def is_prime(number):
    is_p = None
    if number == 1:
        is_p = False
    elif number == 2:
        is_p = True
    elif number > 2:
        for n in range(2,number):
            if number % n == 0:
                is_p = False
                break
            else:
                is_p = True
    else:
        return "Number needs to be positive!"
    return is_p

print(is_prime(1))
print(is_prime(3))
print(is_prime(6))