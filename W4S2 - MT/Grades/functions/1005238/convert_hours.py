def convert_hours(total_hours):
    weeks = (total_hours//24)//7
    days = (total_hours//24)-(weeks*7)
    hours = total_hours-(days*24)-(weeks*24*7)
    return weeks, days, hours

print(convert_hours(7))
print(convert_hours(55))
print(convert_hours(247))