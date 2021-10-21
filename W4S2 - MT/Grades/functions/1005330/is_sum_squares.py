def is_prime(number):
    divisors_list = []
    for divisor in range(1,number + 1):
        if(number % divisor == 0):
            divisors_list.append(divisor)
            
    if(len(divisors_list) == 1): 
        is_p = False
    elif(len(divisors_list) > 2):
        is_p = False
    else:
        is_p = True   
    return is_p