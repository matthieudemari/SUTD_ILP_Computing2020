def is_leap_year(year):
    year = str(year)
    n = int(year[3])

    for n in year:
        year = str(year)
        n = int(year[3])
        year = int(year)
        if year%400 == 0:
            is_ly = True
            return is_ly
        
        elif year%100 ==0:
            is_ly = False
            return is_ly
            
        if year%4 ==0:
            is_ly = True
            return is_ly
        
        elif n== 1 or n==3 or n==5 or n==7 or n==9:
            is_ly = False
            return is_ly
 
    return n
    return year
