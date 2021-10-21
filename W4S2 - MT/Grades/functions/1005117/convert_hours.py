def convert_seconds(total_seconds):
    hours = total_seconds//(60*60)
    total_seconds -= hours*(60*60)
    minutes = total_seconds//60
    total_seconds -= minutes*60
    seconds = total_seconds
    return hours, minutes, seconds