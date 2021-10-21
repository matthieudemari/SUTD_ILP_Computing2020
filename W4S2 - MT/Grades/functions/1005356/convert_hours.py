def convert_hours(total_hours): 
    weeks = total_hours / 168 
    weeks= int(weeks)
    days = (total_hours - (weeks * 168)) / 24 
    days= int(days)
    hours = (total_hours - (weeks *168) - (days*24)) 
    hours = int(hours)
    return weeks, days, hours