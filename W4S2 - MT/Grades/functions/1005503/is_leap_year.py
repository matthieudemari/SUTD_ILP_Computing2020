def is_leap_year(year):
    #first test
    bool1 = None
    bool2 = None
    bool3 = None
    is_ly = None
    if year%4 == 0:
        bool1 = True
    else:
        bool1 = False
    #second test
    if year%400 ==0:
        bool2 = True
    else:
        bool2 = False
    #third test
    if year%100 == 0:
        bool3 = True
    else:
        bool3 = False
    #conclusion
    if bool1 == True and bool3 == False or bool2 == True and bool3 == True:
        is_ly = True
    else: 
        is_ly = False
    
    return is_ly