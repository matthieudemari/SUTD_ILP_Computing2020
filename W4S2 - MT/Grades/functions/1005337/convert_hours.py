def convert_seconds(total_seconds):
    if (total_seconds >= 3600):
        while (total_seconds >= 3600):
            hours = total_seconds % 3600
            while (remaining_seconds > 60):
                    remaining_seconds = total_seconds - (hours*3600)
                    minutes = (total_seconds-((hours*3600))) % 60
                    while (remaining_seconds2 > 0):
                        remaining_seconds2 = remaining_seconds - (minutes * 60)
                        seconds = (total_seconds-(minutes*60))
                        return hours, minutes, seconds
    elif (total_seconds >= 60):
        hours = 0
        while (total_seconds > 60):
            minutes = total_seconds % 60
            remaining_seconds2 = total_seconds - (minutes * 60)
            while (remaining_seconds2 > 0):
                seconds = (total_seconds-(minutes*60))
                return hours, minutes, seconds
    elif (total_seconds >= 0):
        hours = 0
        minutes = 0
        seconds = (total_seconds)
    return hours, minutes, seconds

print(convert_seconds(7))
print(convert_seconds(67))
print(convert_seconds(1024))