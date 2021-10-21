def how_many_months(initial_amount, rate):
    months = 0
    initial_amountx = initial_amount
    while initial_amountx<1000000:
        initial_amountx=initial_amountx*(1+rate/100)
        months = months + 1

    return months

print(how_many_months(10000, 1.0))
print(how_many_months(10000, 5.0))
print(how_many_months(100000, 5.0))
print(how_many_months(1000000, 5.0))

Answer:
463
95
48
0