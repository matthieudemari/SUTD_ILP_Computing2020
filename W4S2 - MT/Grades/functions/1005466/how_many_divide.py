from numpy import log
def how_many_months(initial_amount, rate):
    months = 0
    final_amount = initial_amount * ((1 + (rate/100))**months)
    
    months = log(final_amount/initial_amount)/log((1 + (rate/100))
                                                  
    return months