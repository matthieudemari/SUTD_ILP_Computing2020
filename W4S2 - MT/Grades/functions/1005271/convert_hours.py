def convert_seconds(total_seconds):
    
    if(total_seconds>=3600):
        hours = total_seconds//3600
        minutes = (total_seconds-hours*3600)//60
        seconds = total_seconds-hours*3600-minutes*50
   
    elif(total_seconds>=60):
        hours=0
        minutes=total_seconds//60
        seconds=total_seconds-(minutes*60)
        
    else:
        hours=0
        minutes=0
        seconds=total_seconds
        
        
    return hours, minutes, seconds

print(convert_seconds(7))
print(convert_seconds(67))
print(convert_seconds(1024))