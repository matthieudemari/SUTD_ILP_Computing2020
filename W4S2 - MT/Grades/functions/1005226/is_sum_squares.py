def is_prime(number):
    divisors = 0
    for value in range (1, number+1):
        if number%value == 0:
            divisors += 1
    is_p = (divisors == 2)
    return is_p