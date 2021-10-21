def convert_hours(total_hours):
    hours = int(total_hours)
    days = int(hours/24)
    weeks = int(days/7)
 
    return weeks, days, hours

print(convert_hours(7))
print(convert_hours(55))
print(convert_hours(247))