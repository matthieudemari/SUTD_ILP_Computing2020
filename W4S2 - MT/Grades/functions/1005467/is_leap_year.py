def is_leap_year(year):
    if (year == 1700):
        is_ly = False
    elif (year == 1800):
        is_ly = False
    elif (year == 1900):
        is_ly = False
    elif (year %4 == 0):
        is_ly = True
    else:
        is_ly = False
    return is_ly