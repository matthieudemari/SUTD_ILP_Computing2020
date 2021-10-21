def convert_hours(total_hours):
    weeks = int(total_hours/168)
    days = int(total_hours/24) - 7*weeks
    hours = total_hours - 7*24*weeks - 24*days 
    return weeks, days, hours