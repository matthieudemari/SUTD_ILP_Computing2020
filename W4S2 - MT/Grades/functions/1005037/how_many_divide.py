def how_many_months(initial_amount, rate):
    balance = initial_amount
    months = 0
    while (balance < 1000000):
        balance *= (1+rate/100)
        months+=1
    return months