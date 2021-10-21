def prime_number():
    number = int(input('Number'))
    if number<0:
        print("Your number must either be zero or ppositive")
        y = 1
        while(number%y ==0):
            y = y+1
            if(number%y>0 and number - y >0):
                print("Your number is not a prime number")
            else:
                print("Your number is a prime number")