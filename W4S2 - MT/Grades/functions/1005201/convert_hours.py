def convert_seconds(total_seconds):
    hours = None
    minutes = None
    seconds = None
    if(total_seconds < 60):
        seconds = total_seconds
        minutes = 0
        hours = 0
    elif(total_seconds >= 60 and total_seconds < 3600):
        seconds = total_seconds % 60
        minutes = (total_seconds - seconds) / 60
        hours = 0
    elif(total_seconds > 3600):
        seconds = (total_seconds % 3600) % 60
        minutes = ((total_seconds % 3600) - seconds) / 60
        hours = (total_seconds - minutes*60 - seconds) / 3600
    return hours, minutes, seconds