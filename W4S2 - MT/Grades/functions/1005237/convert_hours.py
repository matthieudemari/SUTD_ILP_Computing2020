def convert_hours(total_hours):
    a = (total_hours//1) 
    b = a//24 
    c = b//7
    hours = a - b*24
    days = b - c*7
    weeks = c
    return weeks, days, hours