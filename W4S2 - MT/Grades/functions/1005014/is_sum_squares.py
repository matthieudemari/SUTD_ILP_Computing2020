def is_prime(number):
    is_p = None 
    if (number==1):
        return False
    elif (number==2):
        return True;
    else:
        for x in range(2,number):
            if(number % x==0):
                return False
        return True          
    return is_p
    