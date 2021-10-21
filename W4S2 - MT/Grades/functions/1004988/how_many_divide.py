def how_many_divide(number):
#    counter = 0
    for i in range(number):
# Is range(number) affected by number = number/2?
#        print(range(int(number)))
#        print("i:", i, "number:", number)
        if(number%2==0):
#            counter += 1
            number = number / 2
        else:
#            return counter
            return i