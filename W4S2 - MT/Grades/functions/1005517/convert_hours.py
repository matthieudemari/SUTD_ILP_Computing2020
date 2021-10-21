def convert_seconds(total_seconds):
    hours = total_seconds//(60*60)
    minutes = (total_seconds-hours*3600)//60
    seconds = (total_seconds-minutes*60 - hours*3600)
    return hours, minutes, seconds