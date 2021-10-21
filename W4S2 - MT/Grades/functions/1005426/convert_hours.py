def convert_hours(total_hours):
    if(total_hours>=168):
        weeks = int(total_hours/168)
        days = int((total_hours - weeks*168)/24)
        hours = int(total_hours - weeks*168 - days*24)
    elif(total_hours>=24):
        weeks = 0
        days = int(total_hours/24)
        hours = int(total_hours - days*24)
    elif(total_hours<24):
        weeks = 0
        days = 0
        hours = int(total_hours)
    return weeks, days, hours