def is_leap_year(year):
    is_ly = True
    
    
    if (year%4 == 0 and year%100 == 0):
        if (year%400 == 0):
            return ("is_ly={}".format(is_ly))
    
        else:
            return ("is_ly={}".format(not is_ly))
        
        
    elif (year%4 == 0):
        return ("is_ly={}".format(is_ly))
        
    else:
        return ("is_ly={}".format(not is_ly))
        
    return is_ly

print(is_leap_year(1996))
print(is_leap_year(1997))
print(is_leap_year(1700))
print(is_leap_year(2000))