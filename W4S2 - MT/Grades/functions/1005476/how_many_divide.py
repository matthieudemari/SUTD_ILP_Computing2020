def how_many_months(initial_amount, rate):
    months = 0
    while initial_amount < 1000000:
        months += 1
        initial_amount *= (1 + rate/100)
    return months