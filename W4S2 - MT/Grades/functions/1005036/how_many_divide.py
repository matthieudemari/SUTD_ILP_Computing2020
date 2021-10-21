def how_many_divide(number):
    numbermax = number
    counter = 0
    while counter*2<=numbermax:
        if number % 2 == 0:
            number /= 2
            counter += 1
        else:
            break
    return counter