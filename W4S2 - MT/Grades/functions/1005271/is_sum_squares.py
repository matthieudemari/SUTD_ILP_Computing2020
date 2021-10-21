def is_prime(number):
    if (number==1):
        is_p = False
        return is_p
    
    else:
        for n in range(2,int(number)):
            remainder=int(number)%n
            while (remainder!=0):
                is_p = True
                if (remainder==0):
                    is_p =False
                    return is_p
                    
                return is_p
