def convert_hours(total_hours):
    weeks = total_hours // 168
    leftover_from_weeks = total_hours % 168
    days = leftover_from_weeks // 24
    hours = leftover_from_weeks % 24
    return weeks, days, hours
