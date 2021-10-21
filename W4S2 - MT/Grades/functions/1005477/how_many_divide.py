def how_many_months(initial_amount, rate):
    months = 0
    given_rate = 1 + rate/100
    
    while(initial_amount < 1000000):
        months += 1
        initial_amount *= given_rate
    
    return months