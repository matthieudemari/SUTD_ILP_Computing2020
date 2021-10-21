def how_many_months(initial_amount, rate):
    months = 0
    interest = 0
    while initial_amount < 10**6:
        months += 1
        interest = initial_amount*(rate/100)
        initial_amount += interest
    return months

print(how_many_months(10000, 1.0))
print(how_many_months(10000, 5.0))
print(how_many_months(100000, 5.0))
print(how_many_months(1000000, 5.0))