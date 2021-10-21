def convert_seconds(total_seconds):
    
    seconds = total_seconds % 60
    
    hours = total_seconds // (60**2)
    minutes = int((total_seconds / (60**2) - hours ) * 60 )
    
    return hours, minutes, seconds

print(convert_seconds(7))
print(convert_seconds(67))
print(convert_seconds(1024))
print(convert_seconds(123))