def how_many_divide(number):
    counter = 0
    while(number % 2 == 0):
        counter += 1
        number = number / 2
    return counter