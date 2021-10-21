def convert_hours(total_hours):
    weeks = total_hours//(24*7)
    days = (total_hours-weeks*7*24)//24
    hours = total_hours%24
    return weeks, days, hours