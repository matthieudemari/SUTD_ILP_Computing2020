def convert_seconds(total_seconds):
    hours = total_seconds//(60**2)
    minutes = (total_seconds-(hours*(60**2)))//(60)
    seconds = (total_seconds-(hours*(60**2))-(minutes*(60)))
    return hours, minutes, seconds

print(convert_seconds(7))
print(convert_seconds(67))
print(convert_seconds(1024))