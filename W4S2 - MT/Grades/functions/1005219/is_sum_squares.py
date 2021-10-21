def is_sum_squares(number):
    sq1_list = []
    sq2_list = []
    sq1 = 0
    while (number - (sq1)**2) >= 0:
        sq1_list.append(sq1)
        sq2_list.append(sq1)
        sq1 = sq1 + 1
    for a in sq1_list:
        for b in sq2_list:
            if (a**2 + b**2) != number:
                is_sq = False
            if (a**2 + b**2) == number:
                is_sq = True
                break
            
    return is_sq