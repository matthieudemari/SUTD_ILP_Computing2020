def is_prime(number):
    is_p = None
    count=0
    
    for i in range(1,number+1):
        if(number%i==0):
            count+=1
           
    if(count==2):
        is_p=True
    else:
        is_p=False
        
    return is_p

print(is_prime(1))
print(is_prime(3))
print(is_prime(6))
