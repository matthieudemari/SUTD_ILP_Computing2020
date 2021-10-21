def convert_hours(total_hours):
    if 24 > total_hours >= 0:
        weeks = 0
        days = 0
        hours = total_hours
        print("Weeks = {}, Days = {}, Hours = {}.".format(weeks,days,hours))
    
    elif 168 >total_hours>=24:
        weeks = 0
        days = total_hours // 24
        hours = total_hours % 24
        print("Weeks = {}, Days = {}, Hours = {}.".format(weeks,days,hours))
        
    else:
        weeks = total_hours // 168
        days = (total_hours % 168) // 24
        hours = total_hours - 168*(total_hours // 168) - 24*((total_hours % 168) // 24)
        print("Weeks = {}, Days = {}, Hours = {}.".format(weeks,days,hours))
        