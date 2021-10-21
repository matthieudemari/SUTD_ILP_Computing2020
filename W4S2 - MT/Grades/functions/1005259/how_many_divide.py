import numpy as np
def how_many_months(initial_amount, rate):
    months = np.log(1000000/initial_amount)/np.log(1+rate/100)
    if(months%1==0):
        return int(months)
    else:
        months = int(months)+1
    return months

print(how_many_months(10000, 1.0))
print(how_many_months(10000, 5.0))
print(how_many_months(100000, 5.0))
print(how_many_months(1000000, 5.0))