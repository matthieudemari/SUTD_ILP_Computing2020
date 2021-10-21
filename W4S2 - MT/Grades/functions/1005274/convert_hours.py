def convert_hours(total_hours):
    total_number_of_days = total_hours//24
    weeks = total_number_of_days//7
    days = total_number_of_days%7
    hours = total_hours%24
    return weeks, days, hours