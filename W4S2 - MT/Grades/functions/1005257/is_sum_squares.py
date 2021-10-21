def is_sum_squares(number):
    square_number = 1
    is_sq = False
    if (number**0.5)%1 == 0:
        is_sq = True
    elif (number**0.5)%1 != 0:
        while square_number < number:
            if ((number-square_number)**0.5)%1 == 0:
                is_sq = True
                break
            else:
                square_number = ((square_number**0.5)+1)**2
    return is_sq