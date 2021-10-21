def is_int(num):
    if num%1==0:
        return True
    else:
        return False
def is_sum_squares(number):
    is_sq = False
    testnums=list(range(int((number/2)**0.5)+1))
    for case in testnums:
        if is_int((number-case**2)**0.5):
            is_sq=True
    return is_sq