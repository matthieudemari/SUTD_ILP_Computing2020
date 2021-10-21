def how_many_months(initial_amount, rate):
    totalsum = initial_amount
    months = 0
    while (totalsum < 1000000):
        months += 1
        totalsum += initial_amount*((1 + (rate/100))**months)
    return months