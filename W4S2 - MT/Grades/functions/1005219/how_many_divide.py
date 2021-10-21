def how_many_divide(number):
    counter = 0
    if number % 2 > 0:
        counter = 0
    while number % 2 == 0:
        number = number/2
        counter += 1
    return counter