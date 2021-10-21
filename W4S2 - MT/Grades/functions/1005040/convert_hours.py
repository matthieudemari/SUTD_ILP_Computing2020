def convert_hours(total_hours):
    weeks=0
    days=0
    hours=0
    if(total_hours > 168 or = 168):
        int(number_1) = total_hours // 168
        weeks += number_1
        int(number_2) = number_1 * 168 // 24
        days += number_2
        int(number_3) = number_2 * 24 
        hours = number_3
        return weeks,days,hours
    elif(total_hours > 24 or = 24):
        int(number_1) = total_hours // 168
        weeks += number_1
        int(number_2) = number_1 * 168 // 24
        days += number_2
        int(number_3) = number_2 * 24 
        hours = number_3
        return weeks,days,hours
    else:
        int(number_1) = total_hours // 168
        weeks += number_1
        int(number_2) = number_1 * 168 // 24
        days += number_2
        int(number_3) = number_2 * 24 
        hours = number_3
        return weeks,days,hours

    weeks = float(weeks)
    days = [total_hours - weeks] * 7/24
    hours = None
    return weeks, days, hours