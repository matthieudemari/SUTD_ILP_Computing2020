def is_prime(number):
    is_p = False
    if number > 1:
        for i in range(2,number):
            if (number % i) == 0:
                is_p = False 
                print(number,"is not a prime number")
                break
            else: 
                is_p = True
                print(number,"is a prime number")  
    else:
        is_p = False
        print(number,"is not a prime number") 