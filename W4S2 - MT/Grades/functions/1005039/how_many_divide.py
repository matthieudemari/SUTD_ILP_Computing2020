def how_many_months(initial_amount, rate):
    months = 0
    goal = 1000000
    interest = 1 + rate/100
    new_amount = initial_amount
    while new_amount < goal:
        months += 1
        new_amount *= interest
        
    return months

print(how_many_months(10000, 1.0))
print(how_many_months(10000, 5.0))
print(how_many_months(100000, 5.0))
print(how_many_months(1000000, 5.0))