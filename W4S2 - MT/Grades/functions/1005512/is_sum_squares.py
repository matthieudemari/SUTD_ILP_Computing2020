def is_sum_squares(number):
    
    if int(number**0.5)**2 == number:
        is_sq = True
    elif int((number/2)**0.5)**2 == number/2:
        is_sq = True
    elif int((number - 1**2)**0.5)**2 == number - 1:
        is_sq = True
    elif int((number - 2**2)**0.5)**2 == number - 2:
        is_sq = True
      
    else:
        is_sq = False
    return is_sq