def convert_seconds(total_seconds):
    hours = total_seconds // 3600
    minutes = (total_seconds // 60) - (hours * 60) 
    seconds = total_seconds - (hours * 3600) - (minutes * 60)
    return hours, minutes, seconds