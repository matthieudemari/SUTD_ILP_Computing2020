def convert_seconds(total_seconds):
    hours = 0
    minutes = 0
    seconds = 0
    if total_seconds < 60 :
        seconds = total_seconds
    elif total_seconds >= 60:
        minutes = total_seconds//60
        seconds = total_seconds - minutes*60
        if minutes >= 60:
            hours = minutes // 60
            minutes = minutes - hours * 60
            seconds = total_seconds - hours*3600 - minutes*60
        
    
    return print("hours = {} ".format(hours)), print("minutes={}" .format(minutes)), print("seconds={}".format(seconds))

print(convert_seconds(7))
print(convert_seconds(67))
print(convert_seconds(1024))