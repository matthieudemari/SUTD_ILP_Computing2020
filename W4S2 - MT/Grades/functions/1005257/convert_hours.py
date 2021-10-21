def convert_hours(total_hours):
    hours_in_a_week = 168
    hours_in_a_day = 24
    weeks = total_hours//hours_in_a_week
    days = (total_hours%hours_in_a_week)//hours_in_a_day
    hours = (total_hours%hours_in_a_day)
    return weeks, days, hours