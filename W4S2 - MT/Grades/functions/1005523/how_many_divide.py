def how_many_divide(number):
    
    counter = 0
    # Remainder division to find out if it is even
    if (number%2 == 0):
        # Keep dividing by 2 and add 1 to counter every time if the number is still even 
        while (number%2 == 0):
            number = number/2
            counter += 1   
            
    else:
        counter = 0
        
    return counter