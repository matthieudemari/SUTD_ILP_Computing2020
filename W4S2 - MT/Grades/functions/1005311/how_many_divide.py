def how_many_divide(number):
    counter = 0
    while(number > 0):
        if (number % 2 == 0):
            number = number/2
            counter += 1
        else:
            number = -1
    
    
    return counter
#Key in number to be received between the brackets()
how_many_divide(18)