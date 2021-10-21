def how_many_divide(number):
    counter = 0
    a = number 
    while (a>0 and a%2 == 0):
        a//=2
        counter+=1
    return counter