def how_many_months(initial_amount, rate):
    months = 0
    final_amount = 0
    
    if (initial_amount < 1000000):
        while final_amount < 1000000:
            months += 1
            final_amount = initial_amount * ((1 + (rate/100))**months)
        
    return(months)