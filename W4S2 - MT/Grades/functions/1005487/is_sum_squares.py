def is_sum_squares(number):
    sq_num_lst = []
    for i in range(number):
        if i**2 <= number:
            sq_num_lst.append(i**2)
    
    for sq_num1 in sq_num_lst:
        for sq_num2 in sq_num_lst:
            if sq_num1 + sq_num2 == number:
                return True
   
    return False