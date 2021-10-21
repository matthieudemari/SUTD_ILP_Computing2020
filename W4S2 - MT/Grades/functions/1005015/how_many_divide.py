import numpy as np
def how_many_months(initial_amount, rate):
    future_value = 1000000
    months = np.log(future_value/initial_amount) - np.log(1 + rate)
    return months