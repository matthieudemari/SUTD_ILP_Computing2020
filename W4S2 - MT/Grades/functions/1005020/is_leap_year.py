def is_leap_year(year):
    is_ly = None
    
    if(year % 400 == 0):
        is_ly = True
    elif(year % 100 == 0):
        is_ly = False
    elif(year % 4 == 0):
        is_ly = True
    else:
        is_ly = False
    
    return is_ly