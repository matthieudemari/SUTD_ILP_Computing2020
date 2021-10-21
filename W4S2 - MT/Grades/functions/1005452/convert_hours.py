def convert_seconds(total_seconds):
    if (total_seconds < 0):
        print("Total time cannot be a negative value. Please try again.")
    elif (0<total_seconds<=60):
        hours = 0
        minutes = 0
        seconds = total_seconds
    elif (60<total_seconds<=3599):
        hours = 0
        minutes = total_seconds//60
        seconds = total_seconds%60
    elif (total_seconds>=3600):
        hours = total_seconds//3600
        minutes = (3600 - (total_seconds//3600)*3600)//60
        seconds = total_seconds%60
    return hours, minutes, seconds