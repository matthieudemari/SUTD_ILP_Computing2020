from numpy import log
import math

def how_many_months(initial_amount, rate):
    months = 0
    if (initial_amount<=0 or rate<=0):
        print("You need to have a positive amount of money in your bank account, together with a positive bank interest rate in order to reach 1 Million dollars.")
    else:
        months = math.ceil((log(1000000/initial_amount))/(log(1+(rate/100))))
    return months