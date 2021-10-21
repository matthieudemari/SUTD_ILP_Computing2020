def convert_hours(total_hours):
    weeks = total_hours//(7*24)
    days = (total_hours%(7*24))//(24))
    hours = total_hours%(24)
    print("week = {}, days = {}, hours = {}".format(weeks, days, hours))