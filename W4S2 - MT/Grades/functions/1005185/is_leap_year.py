def is_leap_year(year):
    
    if(year%400==0):
        is_ly = True
        
    elif(year%4==0 and year%100!=0):
        is_ly=True
        
    else:
        is_ly=False
        
    return is_ly