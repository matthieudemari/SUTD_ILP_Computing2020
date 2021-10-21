def is_prime(number):
    
    is_p= True
    
    if number ==1:
        is_p = False
        
    elif number > 1:
        a = [1,2,3,4,5,6,7,8,9,10]
        counter=0
        for val in a:
            if number%val ==0 :
                counter+=1
        if counter>2:
            is_p= False

        
    return is_p

print(is_prime(1))
print(is_prime(3))
print(is_prime(6))