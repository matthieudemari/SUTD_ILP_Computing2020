def convert_hours(total_hours):
    
    if (total_hours>0):
        week_hours = 168
        day_hours = 24
        weeks = 0
        days = 0
        hours = 0
        
        while(total_hours > week_hours):
            total_hours -= week_hours
            weeks += 1
        
        while (total_hours > day_hours):
            total_hours -= day_hours
            days += 1
            
        if (total_hours > 0):
            hours = total_hours

    return weeks, days, hours

print(convert_hours(7))
print(convert_hours(55))
print(convert_hours(247))