def how_many_divide(number):
    counter = 0
    while(number % 2 == 0):
        number = number / 2
        counter += 1
        #print(number)
        #print(counter)
        #print("_____")
    return counter