def how_many_divide(number):
    counter = 0
    
    if number <= 0:
        print("thats not a strictly positive number")
    else:
        while (number%2 == 0):
            number = number/2
            counter += 1
    
    return counter