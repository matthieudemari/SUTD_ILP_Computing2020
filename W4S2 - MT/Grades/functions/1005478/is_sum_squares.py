def is_prime(number):
    if(number/2==3):
        if(number/3==2):
            if(number/number==1):
                is_p=True
        is_p= True
        
    else:
        is_p= False
    
    return is_p

print(is_prime(1))
print(is_prime(3))
print(is_prime(6))