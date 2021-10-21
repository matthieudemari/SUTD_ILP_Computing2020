def convert_seconds(total_seconds):
    if(total_seconds >= 3600):
        hours = total_seconds // 3600
        minutes = (total_seconds - hours*3600) // 60
        seconds = (total_seconds - hours*3600 - minutes*60)
    elif(total_seconds < 60):
        hours = 0
        minutes = 0
        seconds = total_seconds
    elif(total_seconds < 3600):
        hours = 0
        minutes = total_seconds // 60
        seconds = (total_seconds - minutes*60)

    return hours, minutes, seconds