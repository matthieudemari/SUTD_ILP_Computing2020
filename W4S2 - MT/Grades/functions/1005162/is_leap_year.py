def is_leap_year(year):
    if (int(year)%400 == 0 or int(year)%4 == 0 and int(year)%100 != 0):
        is_ly = True
    else:
        is_ly = False
    return is_ly

print(is_leap_year(1996))
print(is_leap_year(1997))
print(is_leap_year(1700))
print(is_leap_year(2000))