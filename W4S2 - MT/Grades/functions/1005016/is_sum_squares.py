def is_sum_squares(number):
    first_sq = int(number**0.5)
    second_sq = int((number-first_sq**2)**0.5)
    is_sq = first_sq**2 + second_sq**2 == number 
    return is_sq