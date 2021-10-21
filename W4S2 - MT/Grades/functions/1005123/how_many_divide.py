def how_many_divide(number):
    counter = 0
    if(number == 0 or number == 1 or number == 3):
        counter = 0
        return counter
        
    if(number == 2):
        counter = counter + 1
        return counter

    else:
        if(number%2 != 0):
            counter = 0
        else:
            while(False):
                number /= 2
                counter += 1
                if(number%2 != 0):
                    break
        return counter

print(how_many_divide(3))
print(how_many_divide(4))
print(how_many_divide(12))
print(how_many_divide(64))