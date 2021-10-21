def is_leap_year(year):
    is_ly = False
    if (year % 4 == 0):
        if (year % 100 == 0):
            is_ly = False
            if (year % 400 == 0):
                is_ly = True
        else:
            is_ly = True

    return is_ly