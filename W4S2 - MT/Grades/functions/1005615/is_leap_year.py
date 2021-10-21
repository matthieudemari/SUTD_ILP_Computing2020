def is_leap_year(year):
    is_ly = False
    if int(year)%4==0:
        return True
    if not int(year)%4==0:
        return False
    return is_ly