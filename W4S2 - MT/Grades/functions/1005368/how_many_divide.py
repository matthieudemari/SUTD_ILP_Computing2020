def how_many_months(initial_amount, rate):
    amount = initial_amount
    months = 0
    while amount<1000000:
        months += 1
        amount = initial_amount*(1+rate/100)**months
    return months

print(how_many_months(10000, 1.0))
print(how_many_months(10000, 5.0))
print(how_many_months(100000, 5.0))
print(how_many_months(1000000, 5.0))