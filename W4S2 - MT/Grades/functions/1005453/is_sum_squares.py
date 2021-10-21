def is_sum_squares(number):
    is_sq = False
    number_sqrt_up = int(number**0.5 + 1)
    
    for num in range(number_sqrt_up):
        for num_2 in range(number_sqrt_up):
            if num**2 + num_2**2 == number:
                is_sq = True
                break
        if is_sq:
            break
            
    return is_sq