def how_many_divide(number):
    counter = 0
    boonlean1 = number%2==0
    
    while (boonlean1):
        counter+=1
        number = number/2
        if (number%2==0):
            boonlean1 = True
        else:
            boonlean1 = False
    
    return counter
print(how_many_divide(3))
print(how_many_divide(4))
print(how_many_divide(12))
print(how_many_divide(64))