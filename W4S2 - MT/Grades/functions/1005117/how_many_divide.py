import math

def how_many_months(initial_amount, rate):
    months = math.ceil((math.log((10**6)/initial_amount)) / (math.log(1 + (rate/100))))
    return months