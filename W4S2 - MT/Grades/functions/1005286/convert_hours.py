def convert_hours(total_hours):
    if total_hours < 24:
        weeks=0
        days=0
        hours=total_hours
        return("weeks={}, days={}, hours={}".format(weeks, days, hours)) 
    
    if (total_hours >= 24 and total_hours < 168):
        weeks=0
        days=total_hours//24
        hours=total_hours%24
        return("weeks={}, days={}, hours={}".format(weeks, days, hours)) 
        
    if total_hours >= 168:
        weeks = total_hours//168
        days = (total_hours-168)//24
        hours = (total_hours-168)%24
        return("weeks={}, days={}, hours={}".format(weeks, days, hours)) 

print(convert_hours(7))
print(convert_hours(55))
print(convert_hours(247))