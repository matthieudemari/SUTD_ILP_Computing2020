def is_leap_year(year):
    is_ly = True
    if year % 400 == 0:
        is_ly = True
    elif year % 100 == 0:
        is_ly = False
    elif year % 4 == 0:
        is_ly = True
    else:
        is_ly = False   
    return is_ly

print(is_leap_year(1996))
print(is_leap_year(1997))
print(is_leap_year(1700))
print(is_leap_year(2000))