def is_leap_year(year):
    if year%10==0:
        if year%400==0:
            is_ly=True
        else:
            is_ly=False
    elif year%4==0:
        is_ly=True
    else:
        is_ly=False
    return is_ly