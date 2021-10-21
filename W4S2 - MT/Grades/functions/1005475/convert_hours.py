def convert_seconds(total_seconds):
    hours = 0
    minutes = 0
    seconds = 0
    
    if total_seconds >= 3600:
        hours = total_seconds//3600
        total_seconds -= hours*3600
        
    if total_seconds >= 60:
        minutes = total_seconds//60
        total_seconds -= minutes*60
        
    else:
        seconds = total_seconds
        total_seconds -= 1
    
    return hours, minutes, seconds

print(convert_seconds(7))
print(convert_seconds(67))
print(convert_seconds(3625))