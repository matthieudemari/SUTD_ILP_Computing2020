def convert_hours(total_hours):
    weeks = int(total_hours/(24*7))
    days = int(total_hours/24%7)
    hours = int(total_hours%24)
    return weeks, days, hours

print(convert_hours(7))
print(convert_hours(55))
print(convert_hours(247))