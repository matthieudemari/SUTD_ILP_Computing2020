def convert_seconds(total_seconds):
    if (total_seconds >= 3600):
        hours = total_seconds//3600
    else:
        hours = 0
    if (total_seconds >= 60):
        minutes = total_seconds//60
    else:
        minutes = 0
    seconds = total_seconds - 60*(total_seconds//60)
    return hours, minutes, seconds