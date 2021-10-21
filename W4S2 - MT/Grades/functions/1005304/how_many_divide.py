def how_many_divide(number):
    counter = 0
    
    # prime number
    for i in range(number):
        if number % i != 0:
            
            while number/2 >= 1:
                number/= 2
                counter += 1
            return counter
    
    # non-prime, divisible by 2
    elif number % 2 == 0:
        while number/2 >= 1:
            number/=  2
            counter += 1
            return counter
    
    # non-prime, non-divisible by 2
    elif number % 2 != 0:
        while number/2 >= 1:
            number/=  2
            counter += 1
            return counter