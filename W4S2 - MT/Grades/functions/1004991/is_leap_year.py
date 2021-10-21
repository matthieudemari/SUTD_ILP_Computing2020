def is_leap_year(year):
    is_ly=False
    if year%400==0:
        is_ly=True
    elif year%100==0:
        is_ly=False
    elif year%4==0:
        is_ly=True
    return is_ly