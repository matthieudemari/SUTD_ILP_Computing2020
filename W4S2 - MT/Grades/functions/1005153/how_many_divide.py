def how_many_months(initial_amount, rate):
    current_amount = initial_amount
    months = 0
    while current_amount < 10**6:
        current_amount *= (1+rate/100)
        months += 1
    return months