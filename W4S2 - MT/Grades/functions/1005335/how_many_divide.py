def how_many_months(initial_amount, rate):
    total_money=initial_amount
    months=0
    while total_money< 1000000:
        months+=1
        total_money=initial_amount*(1+rate/100)**months
    return months