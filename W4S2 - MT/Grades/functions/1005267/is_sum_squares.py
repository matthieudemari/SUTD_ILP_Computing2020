def is_sum_squares(number):
    a = [0,1,2,3,4,5,6,7,8,9]
    b = [0,1,2,3,4,5,6,7,8,9]
    for i in a:
        for j in b:
            if i**2 + j**2 == number:
                is_sq = True
            else:
                is_sq = False
            
    return is_sq

print(is_sum_squares(9))
print(is_sum_squares(5))
print(is_sum_squares(50))
print(is_sum_squares(7))