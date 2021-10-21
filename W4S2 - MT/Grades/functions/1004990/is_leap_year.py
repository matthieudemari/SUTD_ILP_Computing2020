def is_leap_year(year):
    bool1=(year%4==0 and year%100!=0)
    bool2=(year%400==0)
    if bool1==True or bool2==True:
        is_ly = True
    else:
        is_ly = False
    return is_ly