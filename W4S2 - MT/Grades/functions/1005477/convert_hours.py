def convert_seconds(total_seconds):
    
    if (total_seconds >= 3600):
        remainder = total_seconds % 3600
        hours = (total_seconds - remainder)/3600
        remainder2 = remainder % 60
        minutes = (remainder - remainder2)/60
        seconds = remainder2
        
    elif(total_seconds >= 60):
        remainder3 = total_seconds % 60
        minutes = (total_seconds - remainder3)/60
        seconds = remainder3
        hours = 0
        
    elif(total_seconds < 60):
        seconds = total_seconds
        hours = 0
        minutes = 0
        
    return hours, minutes, seconds