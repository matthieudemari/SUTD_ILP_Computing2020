def convert_hours(total_hours):
    weeks = total_hours//24//7
    days = total_hours//24 - (weeks*7)
    hours = total_hours - (weeks*7*24) - (days*24)
    return weeks, days, hours