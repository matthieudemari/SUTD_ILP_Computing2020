def convert_hours(total_hours):
    weeks = int(total_hours/24/7)
    days = int(total_hours/24)
    hours = total_hours%
    return weeks, days, hours

print(convert_hours(7))
print(convert_hours(55))
print(convert_hours(247))