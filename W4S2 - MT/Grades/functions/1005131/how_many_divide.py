def how_many_months(initial_amount, rate):
    months = 0
    amount = initial_amount*(rate+(rate/100)) 
    if(amount<=1000000):
        amount = initial_amount*(rate+(rate/100))
        months+=1
    
    return months
