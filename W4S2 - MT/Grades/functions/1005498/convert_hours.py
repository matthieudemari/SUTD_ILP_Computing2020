def convert_hours(total_hours):
    weeks = total_hours//(24*7)
    
    leftover= total_hours%(24*7)
    
    days = leftover//(24)
    
    hours = leftover%24
    
    return weeks, days, hours

print(convert_hours(7))
print(convert_hours(55))
print(convert_hours(247))