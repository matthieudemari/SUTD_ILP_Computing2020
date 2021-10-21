def is_leap_year(year):
    is_ly = False
    
    if year%4!=0:
        return is_ly
    if year%4==0 and year%100==0 and year%400!=0:
        return is_ly
    else:
        return not is_ly
    

print(is_leap_year(1996))
print(is_leap_year(1997))
print(is_leap_year(1700))
print(is_leap_year(2000))