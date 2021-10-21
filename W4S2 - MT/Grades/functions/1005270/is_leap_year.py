def is_leap_year(year):
    is_ly = (year%100 > 0 and year%4 == 0 or year%400 ==0)
    return is_ly