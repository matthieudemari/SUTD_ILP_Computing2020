def is_leap_year(year):
    
    if year%400==0:
        return True
    else:
        if year %4 ==0:
            if year %100 ==0:
                return False
            else:
                return True
        else:
            return False
    

print(is_leap_year(1996))
print(is_leap_year(1997))
print(is_leap_year(1700))
print(is_leap_year(2000))