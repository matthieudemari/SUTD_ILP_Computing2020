def convert_hours(total_hours):
    weeks = None
    days = None
    hours = None
    if total_hours < 24 and total_hours >= 0:
        print("weeks =0, days =0, hours = {}".format(total_hours))
    elif total_hours >=24 and total_hours < 168:
        days = total_hours//24
        #print(days)
        hours = total_hours - 24*days 
        #print(hours)
        print("weeks =0, days = {}, hours = {}".format(days,hours))
    elif total_hours >= 168:
        weeks = total_hours//168
        #print(weeks)
        days = (total_hours - 168)//24
        #print(days)
        hours = (total_hours - 168) - days*24
        print("weeks =0, days = {}, hours = {}".format(weeks,days,hours))
    return weeks, days, hours