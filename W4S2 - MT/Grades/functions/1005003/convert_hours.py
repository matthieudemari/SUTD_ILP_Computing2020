def convert_seconds(total_seconds):
    total_seconds>0
    hours = total_seconds//3600
    total_seconds%= 3600
    minutes = total_seconds//60
    total_seconds%=60
    seconds = total_seconds%60
    return hours, minutes, seconds

print(convert_seconds(7))
print(convert_seconds(67))
print(convert_seconds(1024))
print (convert_seconds(3625))