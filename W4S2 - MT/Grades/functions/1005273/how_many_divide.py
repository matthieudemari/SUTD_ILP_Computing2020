def how_many_months(initial_amount, rate):
    months = 0
    deposit = initial_amount
    #print (deposit, initial_amount)
    #ensure all entries are positives
    if (initial_amount > 0 and rate > 0):
        while (initial_amount < 1000000 ):
            months += 1
            end_sum = deposit*( 1 + (rate / 100 ) )** months
            initial_amount = end_sum
        return months
    
    #display error message if values are negative
    else:
        print("Amount and interest rates cannot be negative")