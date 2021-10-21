def is_leap_year(year):
    if year%400 ==0:
        is_ly = True
    elif (year -1996)%4 == 0:
        is_ly = True
    else:
        is_ly = False
    return is_ly