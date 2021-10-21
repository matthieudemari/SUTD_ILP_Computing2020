def convert_seconds(total_seconds):
    hours = total_seconds//3600 # floor division to find the number of hours that "fits"
    minutes = (total_seconds - hours*3600)//60 # same, but operated on the remainder
    seconds = total_seconds - hours*3600 - minutes*60 # subtract hours and minutes to find seconds
    return hours, minutes, seconds