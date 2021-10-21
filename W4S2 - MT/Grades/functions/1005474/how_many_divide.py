def how_many_months(initial_amount, rate):
    months = 0
    amount_in_bank = initial_amount*(rate/100)**months
    while (amount_in_bank<1000000):
        months +=1
    return months