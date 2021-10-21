def convert_hours(total_hours):
    weeks = 0
    days = 0
    hours = 0
    
    #less than a day
    if total_hours < 24:
        hours = total_hours
    
    #less than a week
    elif total_hours < (24*7):
        days = total_hours // 24
        hours = total_hours - (days*24)
    
    #more than a week
    elif total_hours >= (24*7):
        weeks = total_hours // (24*7)
        rem_hours = total_hours - (weeks*24*7)
        days = rem_hours // 24
        hours = rem_hours - (days*24)
    
    print("weeks = {}, days = {}, hours = {}".format(weeks, days, hours))
    return weeks, days, hours