def how_many_divide(number):
    number_copy = number
    counter = 0
    if number_copy%2!=0:
        pass
    else:
        while number_copy%2==0:
            number_copy =number_copy/2
            counter+=1

    return counter