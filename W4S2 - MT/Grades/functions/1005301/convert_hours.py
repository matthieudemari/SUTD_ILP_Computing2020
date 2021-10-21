def convert_hours(total_hours):
    weeks = total_hours // (7*24)
    total_hours = total_hours % (7*24)
    days = total_hours // 24
    total_hours = total_hours % 24
    hours = total_hours
    return weeks, days, hours

print(convert_hours(7))
print(convert_hours(55))
print(convert_hours(247))