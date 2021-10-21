def how_many_months(initial_amount, rate):
    months = 0
    
    Compound = initial_amount * (1 + (rate/100))**months
    while Compound <1000000:
        months += 1
        
        
        
    return months
        
        
    

print(how_many_months(10000, 1.0))
print(how_many_months(10000, 5.0))
print(how_many_months(100000, 5.0))
print(how_many_months(1000000, 5.0))