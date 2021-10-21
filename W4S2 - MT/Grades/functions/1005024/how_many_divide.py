def how_many_divide(number):
    counter = 0
    bool1 = (number%2 == 0)
    
    if bool1:
        while number%2 == 0:
            counter += 1
            number = number/2
            if number/2 == 1:
                bool1 = False

        
    return counter