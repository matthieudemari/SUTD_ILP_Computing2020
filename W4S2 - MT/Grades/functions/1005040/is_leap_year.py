def is_leap_year(year):
    if(year % 4 == 0 and year %100 != 0):
        is_ly= True
        return is_ly    
    elif(year % 400 == 0):
        is_ly= True
        return is_ly  