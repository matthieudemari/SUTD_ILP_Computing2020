def how_many_months(initial_amount, rate):
    total_amount= initial_amount
    months = 0
    while (total_amount < 1000000):
        total_amount *= (1 + (rate/100))
        months += 1
    return months