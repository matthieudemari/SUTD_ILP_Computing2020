from numpy import floor, ceil

def is_prime(number):
    is_p = None
    counter=0
    for i in range(2, int(ceil(number**0.5))):
        if (number%i==0):
            counter+=1
        else:
            counter=0
    if (number==1):
        is_p=False
    elif (counter==0):
        is_p=True
    else:
        is_p=False
    
    return is_p

print(is_prime(1))
print(is_prime(3))
print(is_prime(6))