def is_prime(number):
    #number is prime or not, true = prime
    n = 0
    list_new = []
    is_p = False
    while (n<=number):
        n+=1
        if number%n == 0:
            list_new.append(n)
    list_prime = [1, number]
    
    if list_prime == list_new:
        is_p = True
 
    return is_p
