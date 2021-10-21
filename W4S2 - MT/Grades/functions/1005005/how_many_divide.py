def how_many_months(initial_amount, rate):
    months = 1
    amount_after_n_months = initial_amount*(1+rate/100)**months
    while (amount_after_n_months < 1000000):
        months = months +1
        amount_after_n_months = initial_amount*(1+rate/100)**months
    print ("months = {}".format(months))