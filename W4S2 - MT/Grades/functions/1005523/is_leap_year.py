def is_leap_year(year):
    is_ly = False
    
    # Start with centurial year to remove non-leap centurial years
    if (year % 100 == 0):
        if (year % 400 == 0):
            is_ly = True
        else: # Non-leap centurial year is now False
            is_ly = False
            
    # Normal years checked
    elif (year % 4 == 0):
        is_ly = True
    else: 
        is_ly = False
        
    return is_ly