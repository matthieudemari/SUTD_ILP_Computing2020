def how_many_months(initial_amount, rate):
    months = 0
    goal = 1000000
    interest = 1 + rate/100
    new_amount = initial_amount
    while new_amount < goal:
        months += 1
        new_amount *= interest

    return months