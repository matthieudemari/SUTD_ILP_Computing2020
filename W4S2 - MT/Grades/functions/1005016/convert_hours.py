def convert_hours(total_hours):
    if(total_hours>0):
        hours_per_week = 7 * 24
        hours_per_day = 24
        weeks = 0
        days = 0
        hours = 0
        #check for how many weeks
        while(total_hours > hours_per_week):
            total_hours-=hours_per_week
            weeks+=1
        #check for how many days
        while(total_hours > hours_per_day):
            total_hours-=hours_per_day
            days+=1
        #remaining hours
        if(total_hours > 0):
            hours = total_hours
        return weeks, days, hours
    else:
        return(0,0,0)