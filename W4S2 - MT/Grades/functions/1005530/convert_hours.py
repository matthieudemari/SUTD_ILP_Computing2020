def convert_hours(total_hours):
    weeks = total_hours//168
    days = (total_hours-168*weeks)//24
    hours = total_hours-24*days-168*weeks
    return weeks, days, hours

print(convert_hours(7))
print(convert_hours(55))
print(convert_hours(247))