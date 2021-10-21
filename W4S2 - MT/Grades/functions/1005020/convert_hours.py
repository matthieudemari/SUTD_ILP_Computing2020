def convert_hours(total_hours):
    weeks = total_hours // (24 * 7)
    total_hours -= weeks * 24 * 7
    days = total_hours // 24
    total_hours -= days * 24
    hours = total_hours
    return weeks, days, hours