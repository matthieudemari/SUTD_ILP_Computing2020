def how_many_divide(number):
    counter=0
    while True:
        divide1=number/2
        divide2=number//2
        if divide1==divide2:
            counter+=1
            number=divide1
            continue
        else:
            break
    return counter