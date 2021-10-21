def how_many_months(initial_amount, rate):
    
    amount=initial_amount
    months=0
    
    while(True):
        if(amount>=1000000):
            break
        months+=1
        amount=amount*(1+rate/100)
        
        
    return months

print(how_many_months(10000, 1.0))
print(how_many_months(10000, 5.0))
print(how_many_months(100000, 5.0))
print(how_many_months(1000000, 5.0))