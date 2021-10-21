def convert_hours(total_hours):
    hours = total_hours % 24
    days = ((total_hours - hours)/24)%7
    weeks = (((total_hours - hours)/24) -days) / 7
    return weeks, days, hours