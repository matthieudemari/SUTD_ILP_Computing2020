def how_many_divide(number):
    counter = 0
    
    while int(number)%2==0:
        counter += 1
        break
    return counter