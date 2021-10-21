def convert_hours(total_hours):
    weeks = 0
    days = 0
    hours = 0
    
    while total_hours > 168 :
        total_hours = total_hours - 168
        weeks = weeks + 1
    while total_hours > 24 :
        total_hours = total_hours - 24
        days = days + 1
    hours = total_hours
    
    return weeks, days, hours