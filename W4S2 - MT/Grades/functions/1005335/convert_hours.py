def convert_seconds(total_seconds):
    if total_seconds<60:
        seconds=total_seconds
        hours=0
        minutes=0
    elif total_seconds>=60:
        s_to_min=total_seconds//60 #changing seconds to min
        seconds= total_seconds-60*s_to_min #number of seconds
        if s_to_min <60:
            hours=0
            minutes=s_to_min
        elif s_to_min>=60:
            hours= s_to_min//60
            minutes= s_to_min-60*hours
    return hours, minutes, seconds