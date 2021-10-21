from numpy import log
def how_many_months(initial_amount, rate):
    if (initial_amount>=1000000):
        months=0
    elif (initial_amount<1000000):
        months = int((log(1000000/initial_amount)/log(1+rate/100)))+1
    return months