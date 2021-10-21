#it doesnt work for my first value D:do w
def is_leap_year(year):
    is_ly = None
    if year % 100 == 1 or year % 400 == 1:
        if year % 4 ==0:
            is_ly = True
        else: 
            is_ly = False
    elif year % 100 == 0 and year % 400 == 0:
        is_ly = True
        
    else: 
        is_ly = False
        
    
    return is_ly