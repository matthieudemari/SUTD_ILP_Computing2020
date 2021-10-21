def convert_seconds(total_seconds):
    hours = total_seconds//3600
    minutes = (total_seconds - 3600*hours)//60
    seconds = total_seconds - 3600*hours - 60*minutes
    return hours, minutes, seconds