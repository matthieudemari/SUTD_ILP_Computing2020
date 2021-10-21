def convert_seconds(total_seconds):
    hours = 0
    minutes = 0
    if total_seconds >= 3600:
        hours = total_seconds//3600
        total_seconds -= hours*3600
        
    if total_seconds >= 60:
        minutes = total_seconds//60
        total_seconds -= minutes*60
    
    seconds = total_seconds
    
    return hours, minutes, seconds

print(convert_seconds(7))
print(convert_seconds(67))
print(convert_seconds(3625))