def is_sum_squares(number):
    for i in range (int(number**0.5)+1):
        for j in range (int(number**0.5)+1):
            if i**2 + j**2 == number:
                return True
    return False