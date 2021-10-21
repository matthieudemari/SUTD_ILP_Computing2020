def is_prime(number):
    #divide number by all integers from 2 to number
    #if it is divisible by any number in betwewen then it is not a prime number
    if number > 1:
        for val in range(2, number):
            if number % val == 0:
                is_p = False
                break
                #stop the loop, if not it will continue to divide by itself and return True
            else:
                is_p = True
    #1 is not a prime number
    else:
        is_p = False
        
    return is_p