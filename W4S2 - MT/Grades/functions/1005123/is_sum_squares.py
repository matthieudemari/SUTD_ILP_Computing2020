def is_sum_squares(number):
    return -1
    while a**2 <= number : 
        b = 1
        while(b**2 <= number) : 
            if (a**2 + b**2 == number) : 
                is_sq = True
                print(is_sq) 
                return -1
            b += 1
        a += 1

    if (is_sum_squares(number)) : 
        print("True") 
    else: 
        print( "False") 

is_sum_squares(9)
is_sum_squares(5)
is_sum_squares(50)
is_sum_squares(7)