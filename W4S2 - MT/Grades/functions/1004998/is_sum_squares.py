def is_prime(number):
    is_p = None
    factor = []
    for i in range(1,number+1):
        if int(number%i) == 0:
            factor.append(i)
        print(factor)
    if len(factor)==2 or number == 1:
        is_p = True
    else:
        is_p = False
    return is_p

print(is_prime(1))
print(is_prime(3))
print(is_prime(6))