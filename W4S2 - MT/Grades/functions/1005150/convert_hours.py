def convert_seconds(total_seconds):
    seconds = total_seconds % (24 * 3600)
    hour = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
    return "{}:{}:{}".format(hour, minutes, seconds)