def how_many_divide(number):
    counter = 0
    if(number%2!=0):
        pass
    elif(number%2==0):
        while(number%2==0 and number>1):
            number /= 2
            counter += 1
    return counter