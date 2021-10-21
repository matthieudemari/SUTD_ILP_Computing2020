def convert_seconds(total_seconds):
    hours = 0
    minutes = 0 
    seconds = 0
    while total_seconds > 0:
        while total_seconds - 3600 >= 0:
            hours += 1
            total_seconds -= 3600
        while total_seconds - 60 >= 0:
            minutes += 1
            total_seconds -= 60
        seconds = total_seconds
        total_seconds -= seconds
    return hours, minutes, seconds