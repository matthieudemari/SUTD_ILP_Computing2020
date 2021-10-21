def convert_seconds(total_seconds):
    hours = total_seconds/(60*60)
    minutes = total_seconds/60
    seconds = total_seconds
    return round(hours), int(minutes), int(seconds)