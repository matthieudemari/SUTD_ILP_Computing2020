def convert_hours(total_hours):
    
    hours = (total_hours%24)
    
    days = ((total_hours//24)%7)
    
    weeks = days//7
    
    return weeks, days, hours