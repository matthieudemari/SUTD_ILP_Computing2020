def convert_hours(total_hours):
    weeks = total_hours//168
    days = (total_hours%168)//24
    hours = ((total_hours%168)%24)
    return weeks, days, hours