from numpy import *

def how_many_months(initial_amount, rate):
    rate = float(rate)
    months = ((log(1000000/initial_amount))/(log(1+rate/100)))
    if round(months) < months:
        months = int(months) +1
    else:
        months = round(months)
    return months