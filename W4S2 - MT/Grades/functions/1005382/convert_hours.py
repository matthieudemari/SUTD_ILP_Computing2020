def convert_seconds(total_seconds):
    hours = int(total_seconds/3600)
    minutes = int((total_seconds-(hours*3600))/60)
    seconds = int(total_seconds-((hours*3600)+(minutes*60)))
    return hours, minutes, seconds

print(convert_seconds(7))
print(convert_seconds(67))
print(convert_seconds(3625))