def how_many_divide(number):
    counter = 0
    while number%2 == 0:
        number = number/2
        counter = counter+1
        if number == 1:
            break
    return counter