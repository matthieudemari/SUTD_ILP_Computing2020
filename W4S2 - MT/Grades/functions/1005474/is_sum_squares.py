def is_prime(number):
    is_p = False
    divisor=[]
    for value in range(1,number):
        if (number%value == 0):
            divisor.append(value)
    divisor.append(number)
    if len(divisor)==2:
        is_p = True
            
    return is_p