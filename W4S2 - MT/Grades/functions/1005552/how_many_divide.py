def how_many_months(initial_amount, rate):
    minimum = 1000000
    months = 0
    if(initial_amount > 0 and rate > 0):
        while(initial_amount < minimum):
            initial_amount = initial_amount * (1 + rate/100)
            months += 1
    return months