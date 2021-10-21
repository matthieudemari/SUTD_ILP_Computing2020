def how_many_divide(number):
    counter = 0
    while number >= 2:
        number /= 2
        if (number % 1 != 0):
            break
        counter += 1
    return counter