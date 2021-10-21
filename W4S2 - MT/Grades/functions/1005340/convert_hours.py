def convert_seconds(total_seconds):
    hours = total_seconds // 3600
    total_seconds %= 3600
    
    minutes = total_seconds // 60
    total_seconds %= 60
    
    seconds = total_seconds
    
    return hours, minutes, seconds

print(convert_seconds(7))
print(convert_seconds(67))
print(convert_seconds(3625))