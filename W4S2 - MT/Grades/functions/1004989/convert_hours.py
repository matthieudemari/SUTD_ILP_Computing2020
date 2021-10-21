def convert_hours(total_hours):
    weeks = total_hours//(7*24)
    days = (total_hours-weeks*(7*24))//24
    hours = total_hours-weeks*(7*24)-days*24
    return weeks, days, hours
