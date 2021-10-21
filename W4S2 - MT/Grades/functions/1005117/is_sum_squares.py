def is_prime(number):
    divisor_list = []
    prime_condition = [1, number]
    for num in range(1, number+1):
        if number%num == 0:
            divisor_list.append(num)
            
    for divisor in divisor_list:
        if divisor not in prime_condition:
            return False
    is_p = True
    return is_p