def convert_hours(total_hours):
    weeks = 0
    days = 0
    hours = 0
    if total_hours < 24:
        hours += total_hours
    else:
        days += total_hours//24
        hours += total_hours % 24
        if days > 7:
            weeks += days//7
            days = days% 7
    return weeks, days, hours

print(convert_hours(7))
print(convert_hours(55))
print(convert_hours(247))