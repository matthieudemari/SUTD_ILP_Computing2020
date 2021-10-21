def how_many_divide(number):
    divider = 2
    counter = 0
    while number%divider==0:
        number/=divider
        counter+=1
    return counter