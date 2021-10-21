def is_prime(number):
    possible_divisors = [value for value in range(2 , (number+1))]
    list_of_divisors = [1]
    
    for divisors in possible_divisors:
        if number%divisors == 0:
            list_of_divisors.append(number)

    is_p = (len(list_of_divisors) ==2)
    return is_p

print(is_prime(1))
print(is_prime(3))
print(is_prime(6))