def is_leap_year(year):
    if(not year%100==0):
        is_ly = year%4==0
    else:
        is_ly = year%400==0
    return is_ly