def how_many_months(initial_amount, rate):
    not_yet = True
    months = 0
    while(not_yet):
        if initial_amount < 1000000:
            initial_amount = initial_amount*(1+rate/100)
            months += 1
        else:
            not_yet = False
    return months