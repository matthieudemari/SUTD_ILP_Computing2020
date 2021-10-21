def convert_seconds(total_seconds):
    hours = total_seconds // 3600
    minutes = (total_seconds - 3600*hours) // 60
    seconds = total_seconds % 60
    return hours, minutes, seconds

print(convert_seconds(7))
print(convert_seconds(67))
print(convert_seconds(1024))