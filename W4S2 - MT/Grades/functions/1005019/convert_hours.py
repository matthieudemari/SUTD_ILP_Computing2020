def convert_hours(total_hours):
    weeks = (total_hours//24)//7
    hours_from_weeks = weeks*7*24
    days = (total_hours//24)
    hours = total_hours
    if total_hours >= weeks:
        days = (total_hours - hours_from_weeks)//24
        hours_from_days = days*24
        hours = total_hours - hours_from_days - hours_from_weeks
    return weeks, days, hours