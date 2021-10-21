def convert_hours(total_hours):
    weeks = total_hours // 168;
    if (total_hours>168):
        days = (total_hours-weeks*168)//24
    else:
        days = total_hours // 24
    if (total_hours>24):
        hours = (total_hours-weeks*168-days*24)
    else:
        hours = total_hours
    return weeks, days, hours

print(convert_hours(7))
print(convert_hours(55))
print(convert_hours(247))