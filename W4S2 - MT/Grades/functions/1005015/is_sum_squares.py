def is_prime(num):
    if num > 1:
        for i in range(2,num):
            boolean1 = (num % i == 0)
            if num % i == 0:
                print(boolean1)
                break
            else:
                print(boolean1)
    return num