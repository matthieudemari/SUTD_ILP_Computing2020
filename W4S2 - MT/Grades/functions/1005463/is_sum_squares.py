def is_prime(number):

    
    if(number >= 2): 
        for element in range(2,number):
            if ((number // element) == 1):
                is_p = True 
                break
    else:
        is_p = False

    return is_p