def convert_seconds(total_seconds):
    if total_seconds<60:
        hours=0
        minutes=0
        seconds= total_seconds
        return  hours, minutes, seconds
        
    elif total_seconds<60*2:
        hours=0
        minutes=int(total_seconds/60)
        seconds=int(total_seconds - minutes*60)
        return  hours, minutes, seconds
    
    else: 
        hours= int(total_seconds/3600)
        minutes= int((total_seconds/60)-60*hours)
        seconds= int(total_seconds - hours*3600 - minutes*60)
        return  hours, minutes, seconds
        
print(convert_seconds(7))
print(convert_seconds(67))
print(convert_seconds(3625))