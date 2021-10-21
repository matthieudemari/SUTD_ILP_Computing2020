def convert_hours(total_hours):
    # Number of hours in a day = 24, 7 days a week. Integer division to find the number of hours a week
    weeks = total_hours // (24*7)
    
    # For larger no, of hours, remove the no. of days the weeks has included alr
    days = (total_hours - weeks*7*24) // 24
    
    # Remainder at the end to find days
    hours = total_hours - weeks*7*24 - days*24
    
    return weeks, days, hours