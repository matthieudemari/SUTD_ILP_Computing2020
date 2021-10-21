def how_many_months(initial_amount, rate):
    months = 0
    final=1000000
    amtrn=initial_amount
    while (amtrn<final):
        amtrn+=amtrn*(rate/100)
        months+=1
    return months

print(how_many_months(10000, 1.0))
print(how_many_months(10000, 5.0))
print(how_many_months(100000, 5.0))
print(how_many_months(1000000, 5.0))