def convert_seconds():
time = int(input('seconds'))
return time
if time<60:
    print(time)
    if time>=60:
        minutes = time/60
        seconds = time%60
        print(time).format(minutes, seconds)
        if time>=3600:
            hours = time/3600
            minutes = (time%3600)/60
            seconds = (time%3600)/60**2
print(time).format(hours, minutes, seconds)