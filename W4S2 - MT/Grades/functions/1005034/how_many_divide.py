def how_many_divide(number):
    counter = 0
    
    while number/2 == round(number/2) :
        number = number/2
        counter += 1
        
    return counter
