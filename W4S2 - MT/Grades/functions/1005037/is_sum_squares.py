def is_prime(number):  
    number_of_divisor = 0
    is_p = None    
    for divisor in range(1,number+1):       
        if (number%divisor==0):
            number_of_divisor +=1    
    if (number<=1):
        is_p = False
    elif (number_of_divisor==2):
        is_p = True
    else:
        is_p = False   
    return is_p