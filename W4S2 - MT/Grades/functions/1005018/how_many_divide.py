def how_many_months(initial_amount, rate):
    #initial final amount is zero 
    final_amount = 0
    months = 0
    
    #have to make sure that the initial amount less than 1000000
    while (final_amount < 1000000 and initial_amount < 1000000):
        months += 1 
        final_amount = initial_amount * (1 + rate/100)**months
        
    return months


print(how_many_months(10000, 1.0))
print(how_many_months(10000, 5.0))
print(how_many_months(100000, 5.0))
print(how_many_months(1000000, 5.0))