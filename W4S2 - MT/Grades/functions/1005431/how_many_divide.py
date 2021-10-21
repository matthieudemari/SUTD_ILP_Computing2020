import math
def how_many_months(initial_amount, rate):
    
    months_decimals = (math.log10(1000000/initial_amount))/(math.log10(1+(rate/100)))
    months = math.ceil(months_decimals)
   
    return months