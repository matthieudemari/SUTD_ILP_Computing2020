def how_many_months(initial_amount, rate):
    from numpy import log
  
    months = log((1*(10**6))/initial_amount)/log((100 + rate)/100) 
      
    return months