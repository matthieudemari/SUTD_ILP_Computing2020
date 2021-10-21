def convert_hours(total_hours):
    weeks = total_hours//168
    days = (total_hours - 168*weeks)//24
    hours = total_hours - 168*weeks - 24*days
    return weeks, days, hours