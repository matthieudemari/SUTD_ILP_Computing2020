def is_leap_year(year):
    is_ly = True
    
    if year%400 == 0:
        return is_ly    
    if year%100 == 0:
        return not is_ly
    if year%4 == 0:
        return is_ly

    else:
        return not is_ly