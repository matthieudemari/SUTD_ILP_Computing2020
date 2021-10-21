def is_prime(number):
    divisors = []
    numbers = list(range(number + 1))
    for num in numbers:
        if num !=0 :
            if number%num ==0:
                divisors.append(num)
    if len(divisors) == 2:
        is_p = True
    else:
        is_p = False
    
    return is_p

print(is_prime(1))
print(is_prime(3))
print(is_prime(6))