def is_prime(number):
    is_p = if (number==1):
        return False

    elif (number==2):
        return True;

    else:
        for x in range(2,number):
            if(number % x==0):
                return False
        return True          
    return is_p

print(is_prime(1))
print(is_prime(3))
print(is_prime(6))