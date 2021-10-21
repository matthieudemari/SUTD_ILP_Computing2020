def how_many_months(initial_amount, rate):
    
    #set months counter to zero
    months = 0
    
    #while value is below 1 million
    while initial_amount < 1000000:
        
        #multiply 1+rate/100
        initial_amount = initial_amount*(1+rate/100)
        print ("amount so far:", initial_amount)
        #add 1 to months counter
        months += 1
        print ("months so far:", months)
    
    return months

print(how_many_months(10000, 1.0))
print(how_many_months(10000, 5.0))
print(how_many_months(1000000, 5.0))