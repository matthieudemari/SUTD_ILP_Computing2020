def convert_seconds(total_seconds):
    #hours
    if total_seconds >=3600:
        hours = total_seconds//3600
        print(hours,"hours")
        remainder = int(((total_seconds/3600)-hours)*60)
        print(remainder,"minutes")
        remainder_sec = round(((((total_seconds/3600)-hours)*60)-remainder)*60)
        print(remainder_sec,"seconds")
        return hours, remainder, remainder_sec
    #minutes
    elif total_seconds >=60:
        print("0 hours")
        minutes = total_seconds//60
        print(minutes,"minutes")
        remainder_sec= int((total_seconds/60-minutes)*60)
        print(remainder_sec,"seconds")
        return minutes, remainder_sec
    
    #seconds
    else:
        print("0 hours")
        print("0 minutes")
        seconds = total_seconds
        print(seconds, "seconds")
        return seconds

print(convert_seconds(7))
print(convert_seconds(67))
print(convert_seconds(3625))