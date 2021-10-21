def convert_hours(total_hours):
    weeks=0
    days=0
    hours=0
    while True:
        if total_hours>=168:
            total_hours-=168
            weeks+=1
        elif total_hours<24:
            total_hours-=1
            hours+=1
            if total_hours==0:
                return weeks, days, hours
        else:
            total_hours-=24
            days+=1