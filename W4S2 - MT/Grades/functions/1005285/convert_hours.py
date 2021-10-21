def convert_hours(total_hours):
    weeks = total_hours//(24*7)
    if total_hours>168:
        days = (total_hours%168)//24
    else:
        days = total_hours//24
    hours = total_hours%24
    return weeks, days, hours