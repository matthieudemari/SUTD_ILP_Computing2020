def convert_seconds(total_seconds):
    if total_seconds >= 3600:
        hours = total_seconds//3600
        remaining_seconds = total_seconds%3600
        if remaining_seconds >=60:
            minutes = remaining_seconds//60
        else:
            seconds = remaining_seconds
    elif total_seconds >= 60:
        minutes = total_seconds//60
        remaining_seconds = total_seconds%60
        seconds = remaining_seconds
    else: 
        seconds = total_seconds
    return hours, minutes, seconds