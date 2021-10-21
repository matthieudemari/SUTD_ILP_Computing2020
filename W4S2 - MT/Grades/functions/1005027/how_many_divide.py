def how_many_months(initial_amount, rate):
    months = 0
    if(initial_amount < 1000000):
        while(initial_amount * (1 + rate/100)**months <= 1000000):
            months += 1
    else:
        months = 0
    return months