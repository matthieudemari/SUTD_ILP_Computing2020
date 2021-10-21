def convert_seconds(total_seconds):
    
    if(total_seconds>=3600):
        print("hours=int(total_seconds//3600")
        print("minutes=int((total_seconds%3600)*60)")
        print("seconds=int((total_seconds%3600)*60*60)")
        
    elif(total_seconds<3600):
        print("minutes=int(total_seconds//60)")
        print("seconds=int((total_seconds%60)*60)")
        
    elif(total_seconds<60):
        print("seconds=int(total_seconds)")
    return hours, minutes, seconds

print(convert_seconds(7))
print(convert_seconds(67))
print(convert_seconds(1024))