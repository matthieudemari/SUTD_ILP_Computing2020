def how_many_divide(number):
    x=0
    if number%2 ==0:
        x=1
        while ((number/2)%2==0):
            number/=2
            x+=1
        print(x)
    else:
        print(x)
        