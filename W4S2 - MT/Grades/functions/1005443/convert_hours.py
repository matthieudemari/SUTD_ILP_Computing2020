def convert_hours(total_hours):
    weeks = 0
    days = 0
    hours = 0
    hours_left = 0
    weeks = total_hours % 168
    hours_left = total_hours-168*weeks
    days = hours_left%24
    hours_left = hours_left-24*days
    hours = hours_left
    return weeks, days, hours