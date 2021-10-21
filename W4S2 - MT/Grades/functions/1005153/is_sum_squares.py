def is_prime(number):
    if number == 1:
        return False
    # Number is prime if it does not have a factor less than its square root
    for factor in range(2,int(number**0.5+1)):
        if number % factor == 0:
            return False
    return True