def is_sum_squares(number):
    a = 0
    is_sq = None
    while(a^2 <= number):
        if(type((number - a^2)**0.5) is int):
            is_sq = True
            break
        a += 1
        return is_sq