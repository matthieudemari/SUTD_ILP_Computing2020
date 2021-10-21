def is_prime(number):
    is_p=True
    if (number<0):
        is_p=False
    elif (number==0):
        is_p=False
    elif (number>0):
        for i in range (2,number):
            if (number%i==0):
                is_p=False
    return is_p