from numpy import log

def how_many_months(initial_amount, rate):
    months = int((log(1000000)-log(initial_amount))/log(1+0.01*rate)) + 1
    return months