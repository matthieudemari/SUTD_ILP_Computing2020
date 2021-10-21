def convert_seconds(total_seconds):
    hours = total_seconds//(60*60)
    minutes = (total_seconds-(hours*60*60))//(60)
    seconds = (total_seconds-(hours*60*60)-(minutes*60))
    return hours, minutes, seconds