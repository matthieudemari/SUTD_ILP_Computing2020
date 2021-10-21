def is_leap_year(year):
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        is_ly = True
    else:
        is_ly = False
    return is_ly
    