def how_many_months(initial_amount, rate):
    amount = initial_amount
    months = 0
    while (amount<1000000):
        amount *= (1+(rate/100))
        months += 1
    return months