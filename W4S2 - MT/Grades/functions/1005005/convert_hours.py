def convert_seconds(total_seconds):
    if (total_seconds>3600 and (total_seconds-3600)>60):
        hours = int(total_seconds/3600)
        minutes = (int(total_seconds-3600)/60)
        seconds = ((total_seconds-3600)/60)%60
    elif (total_seconds>3600 and (total_seconds-3600)<60):
        hours = int(total_seconds/3600)
        minutes = 0
        seconds = total_seconds%3600
    elif (total_seconds<3600 and total_seconds>60):
        hours = 0
        minutes = int(total_seconds/60)
        seconds = total_seconds%60
    elif (total_seconds<60):
        hours = 0
        minutes = 0
        seconds = total_seconds%60   
    
    print ("hours={}, minutes={}, seconds={}".format(hours, minutes, seconds))