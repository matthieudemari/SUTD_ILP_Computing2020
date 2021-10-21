def is_leap_year(year):
    is_ly = False
    divide4 = year%4 == 0
    divide100 = year%100 == 0
    divide400 = year%400 == 0
    if divide4 and not divide100:
        is_ly = True
    elif divide4 and divide400:
        is_ly = True
    else:
        is_ly = False
    return is_ly
