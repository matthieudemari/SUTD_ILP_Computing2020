def convert_seconds(total_seconds):
    #find number of (3600 second sets) = number of hours
    hours = total_seconds // 3600
    #minus off hours*3600, find number of (60 second sets) in remainder = number of minutes
    minutes = (total_seconds - hours*3600) // 60
    #minus off hours*3600 and minutes*60 = number of seconds
    seconds = total_seconds - hours*3600 - (minutes*60)
    return hours, minutes, seconds