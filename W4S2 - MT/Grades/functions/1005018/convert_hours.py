def convert_seconds(total_seconds):
    #since 1 hour equals to 3600s and 1 min equals to 60s
    hours = int(total_seconds/3600)
    #time left in seconds after minus hour
    total_seconds = total_seconds-3600*hours
    
    minutes = int(total_seconds/60)
    #time left in seconds after minus minutes
    total_seconds = total_seconds-60*minutes
    
    seconds = int(total_seconds)
    return hours, minutes, seconds

print(convert_seconds(7))
print(convert_seconds(67))
print(convert_seconds(3625))