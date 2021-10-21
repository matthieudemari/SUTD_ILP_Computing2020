def convert_seconds(total_seconds): 
    hours = (total_seconds-(total_seconds%3600))//3600
    minutes = (total_seconds-(total_seconds%60))//60
    seconds = total_seconds % 3600
    return hours, minutes, seconds
