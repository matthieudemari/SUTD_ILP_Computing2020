def convert_hours(total_hours):
    weeks = total_hours // 168
    total_hours -= weeks*168 
    days = total_hours // 24
    hours = total_hours - days*24
    return weeks, days, hours
