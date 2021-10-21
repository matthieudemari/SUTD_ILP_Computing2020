def convert_hours(total_hours):
    if total_hours >= 168:
        weeks = total_hours//168
    if total_hours >= 24:
        days = total_hours//24
    hours = total_hours
    return weeks, days, hours

print(convert_hours(total_hours=7))
print(convert_hours(total_hours=55))
print(convert_hours(total_hours=247))