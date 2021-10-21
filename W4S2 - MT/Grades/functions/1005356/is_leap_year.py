def is_leap_year(year):
    bool1 = ((year % 4) == 0) 
    bool1 = True
    bool2 = ((year % 100) == 0) 
    bool2 = False
    bool3 = ((year % 400) == 0)
    bool3 = True
    
    is_ly = bool1 and bool2 and bool3
    return is_ly