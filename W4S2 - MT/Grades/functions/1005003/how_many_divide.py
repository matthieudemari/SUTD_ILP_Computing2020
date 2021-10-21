import math

def how_many_months(initial_amount, rate):
    initial_amount>0
    rate>0
    months = math.log(1000000/initial_amount, (1+rate/100))
    return months

print(how_many_months(10000, 1.0))
print(how_many_months(10000, 5.0))
print(how_many_months(100000, 5.0))
print(how_many_months(1000000, 5.0))