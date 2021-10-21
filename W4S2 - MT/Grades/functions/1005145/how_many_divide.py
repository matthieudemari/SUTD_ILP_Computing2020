def how_many_months(initial_amount, rate):
    months = 0 
    amount = initial_amount
    while (amount < 1000000):
        months += 1
        amount = amount * (1+rate/100)
    return (months)