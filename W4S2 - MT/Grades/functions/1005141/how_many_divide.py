def how_many_divide(number):
    counter = 0
    while (number % 2**counter == 0):
        counter += 1
    else:    
        return print(counter - 1)