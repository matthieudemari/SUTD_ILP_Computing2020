def is_sum_squares(number):
    from numpy import sqrt 
    # Check if number can sqrt
    # Check if number can sqrt after removing other squares
    sq_number = sqrt(number)
    sq2_number = sqrt(number - 1)
    sq3_number = sqrt(number - 2**2)
    sq4_number = sqrt(number - 3**2)
    sq5_number = sqrt(number - 4**2)
    sq6_number = sqrt(number - 5**2)
    sq7_number = sqrt(number - 6**2)
    
    # Rounding of number stays the same
    if (sq_number and sq2_number and sq3_number and sq4_number and sq5_number and sq6_number and sq7_number <=0):
        is_sq = False
    
    elif sq_number == round(sq_number):
        is_sq = True
    
    elif sq2_number == round(sq2_number):
        is_sq = True
        
    elif sq3_number == round(sq3_number):
        is_sq = True
        
# Error here because number you are sqrt is negative....    
elif sq4_number == round(sq4_number):
        is_sq = True
        
    elif sq5_number == round(sq5_number):
        is_sq = True
        
    elif sq6_number == round(sq6_number):
        is_sq = True
    
    else:
        is_sq = False
        
    return is_sq