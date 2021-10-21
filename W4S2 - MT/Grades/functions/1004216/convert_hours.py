def convert_hours(total_hours):
    hours = total_hours
    days = int(total_hours / 24)
    weeks = int(days / 7)
    
    return hours, days, weeks