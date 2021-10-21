def is_leap_year(year):
    #case 1 is when the year is divisible by 100
    
    #case 2 is when the year is divisible by 4
    
    is_ly = (year%100 == 0 and year%400 == 0) or (year%4 == 0 and year%100 != 0)
      
    return is_ly