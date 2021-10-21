def convert_hours(total_hours):
    
    # total hours in a week = 24 x 7 hours = 168 hours
    weeks = total_hours // 168
    days = (total_hours%168)//24
    hours = (total_hours%168)%24
    weeks1 = "weeks = {}".format(weeks)
    days1 = "days = {}".format(days)
    hours1 = "hours = {}".format(hours)
    # print(weeks1, days1, hours1) ?
    
    return weeks1, days1, hours1 
