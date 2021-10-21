def is_sum_squares(number):
    
    first_no = 0
    
    while (first_no*first_no <= number):
        
        second_no = 0
        
        while (second_no*second_no <= number):
        
            if ((first_no*first_no) + (second_no*second_no) == number):
                
                return True
            
            second_no = second_no + 1
        first_no = first_no + 1
    
    return False

print(is_sum_squares(9))
print(is_sum_squares(5))
print(is_sum_squares(50))
print(is_sum_squares(7))