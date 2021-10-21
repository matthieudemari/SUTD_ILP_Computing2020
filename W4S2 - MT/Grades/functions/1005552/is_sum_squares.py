def is_prime(number):
    counter = 0   
    for element in range(1,number+1,1):

        if((number%element) == 0):
            counter += 1
        else:
            counter = counter
        print(counter)
    if counter == 2:
        is_p = True
    else:
        is_p = False
    return is_p