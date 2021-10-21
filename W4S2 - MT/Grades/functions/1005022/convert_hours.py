def convert_hours(total_hours):
    weeks = int(total_hours/(24*7))
    days = int(total_hours%(24*7)/24)
    hours = int(total_hours%(24*7)%24)
    return weeks, days, hours