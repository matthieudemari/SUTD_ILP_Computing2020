def is_leap_year(year):
    is_ly = False
    if(year%4==0):
        is_ly = True
        if(year%100!=0):
            pass
        elif(year%100==0):
            if(year%400==0):
                pass
            elif(year%400!=0):
                is_ly = False
    elif(year%4!=0):
        pass
    return is_ly

print(is_leap_year(1996))
print(is_leap_year(1997))
print(is_leap_year(1700))
print(is_leap_year(2000))