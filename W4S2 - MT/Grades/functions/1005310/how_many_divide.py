def how_many_divide(number):
    counter = 0
    
    while(True):
        value = number%2
        

        if(value != 0):
            return counter
    
        elif(value == 0):
            counter += 1
            number -= number//2
            
    return counter
