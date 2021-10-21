def convert_hours(total_hours):
    weeks = (total_hours//24)//7
    # number of hours in this number of weeks
    nweeks = weeks*7*24
    days = (total_hours//24)
    hours = total_hours
    if total_hours>=weeks:
        days = (total_hours-nweeks)//24
        #number of hours in this number of days
        ndays = days*24
        hours = total_hours-ndays-nweeks
        return weeks, days, hours
    

print(convert_hours(7))
print(convert_hours(55))
print(convert_hours(247))