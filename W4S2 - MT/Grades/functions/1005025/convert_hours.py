def convert_hours(total_hours):
    if total_hours >= 0:
        weeks = (total_hours//168)
        remaining_hours1 = total_hours - 168*weeks
        days = (remaining_hours1//24)
        remaining_hours2 = remaining_hours1 - 24*days
        hours = remaining_hours2
        return weeks, days, hours
    else:
        print('Invalid')
        return None