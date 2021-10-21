def convert_seconds(total_seconds):
    
    hours = total_seconds//3600
    total_seconds = total_seconds - (hours*3600)
    minutes = total_seconds//60
    total_seconds = total_seconds - (minutes*60)
    seconds = total_seconds
    
    return hours, minutes, seconds