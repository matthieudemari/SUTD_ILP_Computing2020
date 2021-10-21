def convert_seconds(total_seconds):
    seconds = total_seconds
    minutes = int(seconds/60) 
    hours = int(minutes/60) or int(seconds/3600)
    return hours, minutes, seconds

print(convert_seconds(7))
print(convert_seconds(67))
print(convert_seconds(3625))