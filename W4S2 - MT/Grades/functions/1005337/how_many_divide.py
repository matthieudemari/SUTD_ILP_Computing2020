def how_many_months(initial_amount, rate):
    from numpy import log
    months = int((log(1000000/initial_amount)/log(1+rate/100)))
    return months

print(how_many_months(10000, 1.0))
print(how_many_months(10000, 5.0))
print(how_many_months(100000, 5.0))
print(how_many_months(1000000, 5.0))