def is_leap_year(year):
    is_year = None
    
    if year / 4 == 1:
        is_year = True
        if year / 100 == 1:
            is_year = False
        elif year / 400 == 1:
            is_year = True
        else:
            is_year = False    
    else:
        is_year = False
        
    return is_year