def how_many_divide(number):
    counter = 0
    while (number/2) > 0:
        if number%2 == 0:
            counter += 1
            number = number/2
        else:
            break
    return counter
print (how_many_divide(64))