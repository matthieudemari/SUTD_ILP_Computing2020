def is_leap_year(year):
    is_ly = None
    if(year%4 == 0 and year%100 != 0):
        is_ly = True
    elif(year%4 == 0 and year%100 == 0 and year%400 != 0):
        is_ly = False
    elif(year%4 == 0 and year%100 == 0 and year%400 == 0):
        is_ly = True  
    elif(year%4 != 0):
        is_ly = False
    return is_ly