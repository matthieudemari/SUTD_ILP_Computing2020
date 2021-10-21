def convert_hours(total_hours):
    weeks = None
    days = None
    hours = None
    if (total_hours < 24):
        hours = total_hours
        days = 0 
        weeks = 0
    elif (total_hours>=24 and total_hours<=168):
        days = total_hours // 24
        hours = total_hours % 24
        weeks = 0  
    elif (total_hours>168 and total_hours<8760):
        weeks = total_hours // 168
        days = (total_hours % 168)//24
        hours = (total_hours % 168)%24

    return weeks, days, hours

print(convert_hours(7))
print(convert_hours(55))
print(convert_hours(247))