def convert_seconds(total_seconds):
    hours = 0
    minutes = 0
    seconds = 0
    
    #check if it is enough min
    if (total_seconds < 60):
        seconds = total_seconds

    #check if it is enough hours
    elif (total_seconds < 3600):
        minutes = total_seconds // 60
        seconds = total_seconds % 60
        
    else:
        hours = total_seconds / 3600
        minutes = (total_seconds % 3600)/60
        seconds = ((total_seconds % 3600))
        #print(hours)
        hours = int(hours)
        minutes = int(minutes)
        seconds  = int(seconds)
    
    return hours, minutes, seconds