def how_many_months(initial_amount, rate):
    #number of months needed to reach
    n = 0
    x = initial_amount*(1 + rate/100)**n
    if (x == 1000000):
        n = 0  
   
    while(x < 1000000):
        n +=1        
        x = initial_amount*(1 + rate/100)**n
   
   
    
    months = n
    return months

