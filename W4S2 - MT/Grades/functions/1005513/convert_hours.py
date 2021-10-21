def convert_hours(total_hours):
    if (total_hours < 24):
        weeks = 0
        days = 0
        hours = total_hours
        print (weeks, days, hours)
    elif (total_hours >= 24 and total_hours < 168):
        weeks = 0
        days = total_hours // 24
        hours = total_hours % 24
        print (weeks, days, hours)
    else:
        weeks = total_hours // 168
        days = (total_hours % 168) // 24
        hours = (total_hours % 168) % 24
        print (weeks, days, hours)
   