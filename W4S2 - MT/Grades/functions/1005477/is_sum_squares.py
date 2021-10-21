def is_prime(number):
    
    if(number == 1):
        is_p = False
        
    elif(number%number == 0 and number%1 == 0):
        counter = 1
        while(counter < number - 1):
            counter += 1
            if(number%counter == 0):
                is_p = False
                break
            elif(not number%counter == 0 and counter == number - 1):
                is_p = True
        
    return is_p