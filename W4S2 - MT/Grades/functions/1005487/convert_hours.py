def convert_hours(total_hours):
    hours_week = 24*7 #hours in a week
    hours_day = 24 #hours in a day
    
    weeks = 0
    days = 0
    hours = 0
    while total_hours > 0:
        if total_hours < hours_day:
            hours += total_hours
            total_hours = 0
        else:
            if total_hours >= hours_week: #enough hours to form week(s)
                weeks = total_hours // hours_week
                total_hours = total_hours % hours_week #update total_hours left
            else: #enough hours to form day(s)
                days = total_hours // hours_day
                total_hours = total_hours % hours_day #update total_hours left
    return weeks, days, hours