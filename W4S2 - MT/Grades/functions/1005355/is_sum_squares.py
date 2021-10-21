from numpy import sqrt
def is_sum_squares(number):
    a = 0
    b = 0 
    if (a**2 + b**2 != number):
        a += 1
        if (a**2 + b**2 > number):
            a = a
    while (a**2 + b**2 < number):
        
        if(a**2 + b**2 != number ):
            
            
            b += 1
            if(a**2 + b**2 == number):
                
                b = b
   
        
    is_sq = (a**2 + b**2 == number)
    return is_sq