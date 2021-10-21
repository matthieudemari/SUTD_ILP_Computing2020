def is_sum_squares(number):
    is_sq = False
    boo1 = True
    while boo1 == True:
        while number - 1 >= 0:
            number = number - 1
            if number >= 0:
                while number - 2*2 > 0:
                    number = number - 2*2
                    if number >= 0:
                        while number - 3*2 > 0:
                            number = number - 3*2
                            is_sq = True
                            return is_sq