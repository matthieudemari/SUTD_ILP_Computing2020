def is_leap_year(year):
    a=(year%4==0)
    b=(year%100==0)
    c=(year%400==0)
    is_ly = (a and (not b)) or (b and c)
    return is_ly
