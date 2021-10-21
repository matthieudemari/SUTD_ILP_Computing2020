def how_many_divide(number):
    counter = 0
    while (number>=2 and number%2==0):
        counter+=1
        number-=2**counter
    return counter
print(how_many_divide(3))
print(how_many_divide(4))
print(how_many_divide(12))
print(how_many_divide(64))