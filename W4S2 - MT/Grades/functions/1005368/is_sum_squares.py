def is_prime(number):
    is_p = True
    if number != 1:
        for i in range(2,number//2+1):
            if number%i==0:
                is_p = False
                break
    else:
        is_p = False
    return is_p

print(is_prime(1))
print(is_prime(3))
print(is_prime(6))
print(is_prime(5939))
print(is_prime(2))