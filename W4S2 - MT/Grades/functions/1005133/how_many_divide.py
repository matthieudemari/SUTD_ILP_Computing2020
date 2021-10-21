def how_many_months(initial_amount, rate):
    target = 1000000 # SGD
    months = 0
    balance = initial_amount
    while(balance < target): # repeat algorithm while bank acc balance less than target
        months += 1
        balance = initial_amount*(1+(rate/100))**months # interest rate formula
    return months