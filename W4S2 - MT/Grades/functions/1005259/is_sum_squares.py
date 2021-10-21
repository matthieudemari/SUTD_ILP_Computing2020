def is_prime(number):
    divisors = [value for value in range(2,int((number+3)/2))]
    #since 1 is always a divisor no matter.
    is_p = False
    #below will find a second divisor if available other than the number itself
    for divise in divisors:
        if(number%divise == 0):
            is_p = False
        else:
            is_p = True
    return is_p

print(is_prime(1))
print(is_prime(3))
print(is_prime(6))