def is_sum_squares(n):
    is_sq = False
    for i in range(n):
        for j in range(n):
            if i*2 + j*2 == n:
                is_sq = True
    return is_sq