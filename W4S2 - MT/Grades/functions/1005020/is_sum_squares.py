def is_sum_squares(number):
    is_sq = False
    for a in range(0, int(number**0.5 + 1)):
        for b in range(0, int(number**0.5 + 1)):
            c = a**2 + b**2
            #print("a:", a**2, "b:", b**2, "c:", c)
            if (c == number):
                is_sq = True
                return is_sq
    return is_sq