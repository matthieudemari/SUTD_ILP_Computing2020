def how_many_divide(number):
    counter = 0
    done=False
    while done==False:
        if number//2==number/2:
            number=number/2
            counter+=1
        else:
            done=True
    return counter