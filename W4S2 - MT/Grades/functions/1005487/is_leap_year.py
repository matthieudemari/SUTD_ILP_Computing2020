def is_leap_year(year):
    if year % 4 == 0: #exactly divisible by 4
        if year % 100 == 0: #exception
            if year % 400 == 0: #exception
                return True
            return False
        return True
    return False