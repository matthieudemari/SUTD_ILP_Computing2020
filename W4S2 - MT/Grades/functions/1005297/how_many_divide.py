from numpy import log
def how_many_divide(number):
    if number%2 == 0:
        counter = int(log(number)/log(2))
    elif number%2 == 1:
        counter = int(log(number/3)/log(2))
    return counter