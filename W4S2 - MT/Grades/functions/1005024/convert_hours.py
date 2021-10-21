def convert_hours(total_hours):
    hours = None
    days = None
    weeks = None
    if total_hours/24 >7:
        weeks = int(total_hours/24/7)
        days = int(total_hours/24 - weeks*7) 
        hours = total_hours - weeks*7*24 - days*24

    elif total_hours/24 < 7:
        weeks = 0
        days = int(total_hours/24)
        hours = total_hours - days*24
        
    return weeks, days, hours
