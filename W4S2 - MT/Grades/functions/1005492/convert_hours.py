def convert_hours(total_hours):
    if total_hours < 24:
        weeks = 0
        days= 0
        hours = total_hours
    elif total_hours > 24 and total_hours < 168:
        weeks = 0
        days = total_hours//24
        hours = total_hours - 24*(days)
    elif total_hours >168:
        weeks = total_hours//168
        days = (total_hours-weeks*(168))//24
        hours = (total_hours-weeks*(168)-days*(24))
    
    return weeks, days, hours
