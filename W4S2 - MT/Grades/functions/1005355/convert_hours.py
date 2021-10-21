def convert_hours(total_hours):
    #every week has 168 hours
    weeks = int(total_hours/168)
    #find the remainder, every day has 24 hours
    days = int((total_hours - weeks*168)/24)
    # find the remainder
    hours = int(total_hours - weeks*168 - days*24)
    return weeks, days, hours