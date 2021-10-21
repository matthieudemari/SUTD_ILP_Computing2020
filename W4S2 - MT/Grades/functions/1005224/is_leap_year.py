def is_leap_year(year):
    is_ly = ((year % 4 == 0 and year % 100 != 0) or (year % 4 == 0 and year % 400 == 0))
    return is_ly