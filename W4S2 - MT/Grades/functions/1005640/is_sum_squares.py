def is_prime(number):
    is_p = True
    
    div = [1]
    div.append(number)
    i = 2
    
    if number <= 1:
        is_p = False
    
    else:
        
        while i <= number:
            if number % i == 0:
                if i not in div:
                    is_p = False
                break
            i+=1
            
        
    return is_p