def is_sum_squares(number):
    squared_list = []
    counter = 0;
    while(counter < 10000):
        squared_list.append(counter*counter)
        counter += 1
        
    for a in squared_list:
        for b in squared_list:
            if(a+b == number):
                return True
    return False
    
print(is_sum_squares(9))
print(is_sum_squares(5))
print(is_sum_squares(50))
print(is_sum_squares(7))