def convert_hours(total_hours):
    weeks = (int(int(total_hours)/(7*24)))
    days = int((int(total_hours) - int(weeks)*7*24) / 24)
    hours = int(total_hours) -(int(weeks)*24*7) - (int(days)*24)
    return weeks, days, hours