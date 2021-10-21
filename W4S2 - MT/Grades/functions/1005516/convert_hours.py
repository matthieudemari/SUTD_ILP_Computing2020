from numpy import floor 
def convert_hours(total_hours):
        weeks= int(floor(total_hours/168))
        days= int(floor((total_hours%168)/24))
        hours= int(floor((total_hours%168)%24))
        print("weeks={}, days={} and hours={}".format(weeks,hours,days))