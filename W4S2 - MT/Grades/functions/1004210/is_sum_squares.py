def is_prime(number):
    is_p = None
    
    count = 0
    list_store = []
    
    # Run through all divisors until it reaches the number itself
    for elem in range(number):
        divisor = elem + 1
        # Append to the list_store if number is divisible by divisor without any remainder
        if (number % divisor == 0):
            list_store.append(divisor)
    
    # Boolean result of the check if list_store only has two values and that these two values are 1 and the number itself
    isPrime = (len(list_store) == 2) and (number in list_store and 1 in list_store)
    if (isPrime):
        is_p = True
    else:
        is_p = False

    return is_p