def convert_hours(total_hours):
    weeks = total_hours // (24*7)
    days = (total_hours % (24*7)) // 24
    hours = (total_hours - (weeks*24*7) - (days*24))
    return weeks, days, hours