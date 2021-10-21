def convert_hours(total_hours):

    weeks = None
    days = None
    hours = None
    if total_hours//168 != 0:
        weeks=total_hours//168
        total_hours-=(weeks*168)
        
    elif total_hours//168 == 0:
        weeks=0
        
        
    if total_hours//24!=0:
        days=total_hours//24
        total_hours-=(days*24)
    elif total_hours//24 == 0:
        days=0
        
            
    if total_hours<24:
        hours=total_hours
                
        
    return weeks, days, hours

print(convert_hours(7))
print(convert_hours(55))
print(convert_hours(247))