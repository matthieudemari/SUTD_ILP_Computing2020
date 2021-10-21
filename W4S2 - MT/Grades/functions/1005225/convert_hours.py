def convert_seconds(total_seconds):
    hours = int(total_seconds/60//60)
    minutes = int(((total_seconds/60/60) - (hours))*60)
    seconds = (total_seconds - hours*60*60 - minutes*60)
    return hours, minutes, seconds

print(convert_seconds(7))
print(convert_seconds(67))
print(convert_seconds(3625))