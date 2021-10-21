def is_prime(number):
    test_for_divisor = 1
    divisor_list = []
    while (test_for_divisor<=number):
        if number % test_for_divisor == 0:
            divisor_list.append(test_for_divisor)
        test_for_divisor += 1
    if len(divisor_list) == 2:
        is_p = True
    else:
        is_p = False
    return is_p