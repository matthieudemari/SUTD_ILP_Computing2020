def how_many_months(initial_amount, rate):
    total_amt=initial_amount
    months=0 #counter
    while (total_amt<1000000):
        months += 1  #counter += 1
        total_amt = initial_amount*(1+rate/100)**(months)
    return months #return counter

print(how_many_months(10000, 1.0))
print(how_many_months(10000, 5.0))
print(how_many_months(100000, 5.0))
print(how_many_months(1000000, 5.0))