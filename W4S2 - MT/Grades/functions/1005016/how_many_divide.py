def how_many_divide(number):
    counter = 0
    while(number > 0 and number%1 == 0):
        number = number/2
        if(number%1 == 0):
            counter +=1
    return counter