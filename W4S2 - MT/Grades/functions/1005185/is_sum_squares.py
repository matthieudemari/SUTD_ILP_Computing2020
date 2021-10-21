
def is_sum_squares(number):

    bool1=True
    is_sq=False
    n=0
    
    while((number-n**2)>0):   
        x=((number-(n**2))**0.5)%1
        
        if(x==0):
            is_sq=True
            
        n+=1
   
    return is_sq
