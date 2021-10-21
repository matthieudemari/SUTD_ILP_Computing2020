def how_many_divide(number):
    counter = 0
    while True:
        if number % 2 ==0:
            counter+=1
            number = number // 2
        else:
            break
    return counter