def convert_seconds(total_seconds):
    hours = int(total_seconds/360)
    minutes = int((total_seconds - hours*(360))/60)
    seconds = int(total_seconds - hours*(360) - minutes*(60))
    return hours, minutes, seconds        