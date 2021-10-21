def is_sum_squares(number):
    is_sq = False
    squares = []
    
    for i in range(round(number**0.5)+1):
        squares.append(i**2)               
    for j in squares:
        if (number-j) in squares:
            is_sq = True
    return is_sq