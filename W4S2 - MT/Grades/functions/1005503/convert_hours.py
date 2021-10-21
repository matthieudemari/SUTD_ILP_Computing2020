def convert_hours(total_hours):
    #hours calculation
    if total_hours < 24:
        hours = total_hours
    if total_hours >= 24:
        hours = total_hours % 24
        
    #days calculation:
    if total_hours >= 24 and total_hours<168:
        days = total_hours //24 
    elif total_hours >=168:
        days1 = total_hours//24
        days = days1 % 7
    else:
        days = 0
        
    #weeks calculation:
    if total_hours >= 168:
        weeks = total_hours//(7*24)
    else:
        weeks = 0
    return weeks, days, hours

