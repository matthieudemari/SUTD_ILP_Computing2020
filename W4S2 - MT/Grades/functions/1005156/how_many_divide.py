def how_many_months(initial_amount, rate):
    months = 0
    x = initial_amount
    while(x < 1000000):
        months += 1
        x = initial_amount*((1+(rate/100))**months)
    return months, x

print(how_many_months(10000, 1.0))
print(how_many_months(10000, 5.0))
print(how_many_months(100000, 5.0))
print(how_many_months(1000000, 5.0))