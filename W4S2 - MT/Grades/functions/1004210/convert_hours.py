def convert_seconds(total_seconds):
    hours = int(total_seconds/(60*60))
    minutes = int(total_seconds/60 - hours*60)
    seconds = int(total_seconds - hours*60*60 - minutes*60)
    return hours, minutes, seconds