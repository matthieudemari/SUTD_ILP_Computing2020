def is_prime(number):
    
    divisors = []
    div = 1
    while(div>0 and div<=number):
        if(number % div ==0):
            divisors.append(div)
        div+=1
        #print(divisors)
        
    if (len(divisors) == 2):
        is_p = True
        #print(is_p)
    else:
        is_p = False
        #print(is_p)
    
    
    #is_p = None
    return is_p

print(is_prime(1))
print(is_prime(3))
print(is_prime(6))