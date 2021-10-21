def how_many_divide(number):
    counter = 0
    while(number != 0):
        if(number%2 == 0):
            number /= 2
            counter += 1
        else:
            return counter