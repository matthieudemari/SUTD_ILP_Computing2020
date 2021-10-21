from numpy import log
def how_many_months(initial_amount, rate):
    x = log(1000000/initial_amount)
    y = log(1+rate/100)
    if initial_amount < 1000000:
        months = int(x/y) + 1
    else: 
        months = int(x/y)
    
    return "months = {}" .format(months)

print(how_many_months(10000, 1.0))
print(how_many_months(10000, 5.0))
print(how_many_months(100000, 5.0))
print(how_many_months(1000000, 5.0))