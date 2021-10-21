def is_sum_squares(number):
    a = 0
    while a*a < number:
        b = 0
        while (b*b  <= number):
            if (a*a + b*b == number):
                return True
            b += 1
        a += 1
    return False
    