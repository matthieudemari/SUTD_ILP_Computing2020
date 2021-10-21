def is_prime(number):
    is_p = True
    divisors = []
    i=1
    
    while i<number:
        i+=1
        if number%i == 0:
            divisors.append(i)
    is_p= not (len(divisors)>2)
    
    if number==0:
        is_p = False
    if number == 1:
        is_p = False
        
    return is_p

print(is_prime(1))
print(is_prime(3))
print(is_prime(6))