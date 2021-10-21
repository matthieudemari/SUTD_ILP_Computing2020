def convert_seconds(total_seconds):
    hours = total_seconds//60//60
    minutes = total_seconds//60
    seconds = total_seconds%60
    return hours, minutes, seconds
