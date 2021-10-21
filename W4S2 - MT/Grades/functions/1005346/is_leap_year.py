def is_leap_year(year):
    is_ly = None
    if(False):
        is_ly=(year%400==0)
    elif(False):
        is_ly=(year%100==0)
    elif(True):
        is_ly=(year%4==0)
    return is_ly
               
print(is_leap_year(1996))
print(is_leap_year(1997))
print(is_leap_year(1700))
print(is_leap_year(2000))