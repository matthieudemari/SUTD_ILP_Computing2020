def is_sum_squares(number):
    is_sq=True
    a=int(number**0.5)
    for a in range(0,a+1):
        b=(number-a**2)
        c=b**0.5
        if c%2==0 or c%2==1:
            is_sq=True
        else:
            is_sq=False
    return is_sq