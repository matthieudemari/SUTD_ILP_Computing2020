def convert_hours(total_hours):
    weeks=0
    days=0
    hours=0
    if total_hours>168:
        weeks = total_hours//168
    total_hours-=weeks*168
    if total_hours>24:
        days = total_hours//24
    total_hours-=days*24
    if total_hours>0:
        hours = total_hours
    return weeks, days, hours