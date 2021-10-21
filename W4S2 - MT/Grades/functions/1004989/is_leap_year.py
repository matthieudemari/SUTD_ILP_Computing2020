def is_leap_year(year):
    is_ly = False
    if year//100==year/100:
        if year//400==year/400:
            is_ly=True
    elif year//4==year/4:
        is_ly=True
    return is_ly