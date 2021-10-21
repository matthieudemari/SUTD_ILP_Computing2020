def convert_hours(total_hours):
    weeks = int(total_hours/168)
    days = int((total_hours-(weeks*168))/24)
    hours = int(total_hours-(weeks*168)-(days*24))
    return weeks, days, hours

print(convert_hours(7))
print(convert_hours(55))
print(convert_hours(247))