def is_leap_year(year):
    
    is_ly = None
    if(year % 100 == 0):
        if(year % 400 == 0):
            is_ly = True
        else:
            is_ly = False
    else:
        is_ly = (year % 4 == 0)
    return is_ly

print(is_leap_year(1996))
print(is_leap_year(1997))
print(is_leap_year(1700))
print(is_leap_year(2000))