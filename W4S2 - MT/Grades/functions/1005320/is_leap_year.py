def is_leap_year(year):
    is_ly = False
    
    if year <= 0:
        print("sorry that's not a strictly positive integer")
    elif year % 400 == 0:
        is_ly = True
    elif year % 4 == 0:
        is_ly = True
        if year % 100 == 0:
            is_ly = False
    else:
        is_ly == False
    
    return is_ly