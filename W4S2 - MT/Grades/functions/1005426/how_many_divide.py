def how_many_divide(number):
    counter = 0
    # If divisible by 2 is a multiple. Counter increase by 1.
    if(number%2 == True):
        counter +=1
        while(number%2>0):
            counter += 1
            break
    return counter