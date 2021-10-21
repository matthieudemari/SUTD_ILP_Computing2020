def how_many_months(initial_amount, rate):
    import ln function from numpy notebook
    months = ("(ln(1000000)-ln(initial_amount))/ln(1+rate/12)")
    return months

print(how_many_months(10000, 1.0))
print(how_many_months(10000, 5.0))
print(how_many_months(100000, 5.0))
print(how_many_months(1000000, 5.0))