def num_squares(number):
    x = 1
    inquisitor = False
    
    while inquisitor == False:
        if number == pow(x,2) + pow (x+1,2):
            return True
        else:
            x +=1
        
    return inquisitor 