def is_leap_year(year):
    if(year%4 == 0  and year%100 == 0):
        print(False)
    if(year%4 == 0 and year%100 != 0 and year%400 == 0):
        print(True)