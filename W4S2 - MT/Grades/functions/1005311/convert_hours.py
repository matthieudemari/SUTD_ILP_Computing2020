def convert_hours(total_hours):
    
#using integer division // we can find the number of weeks 

    weeks = total_hours//(7*24)

#using modulus % to find the remainder after division, we can find the number of days 

    days = (total_hours%(7*24))//(24)
    hours = total_hours%(24)
    print("week = {}, days = {}, hours = {}".format(weeks, days, hours))
    
#to call the function convert_hours, type a value for the total hours in the brackets, in this case i used 300

convert_hours(300)