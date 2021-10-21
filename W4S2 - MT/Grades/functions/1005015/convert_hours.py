def convert_seconds(total_seconds):
    hours = (total_seconds // 3600)
    minutes = (total_seconds // 60)
    seconds = total_seconds
    while seconds >= 60:
        seconds -= 60
        minutes += 1
    return hours, minutes, seconds