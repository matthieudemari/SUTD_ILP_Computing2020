def are_all_consecutive(my_list):
    
    is_con = False
    
    if len(my_list) <=1 :
        is_con = True
        
    elif len(my_list)> 1:
        n_0 = 0
        n_1 = 1
        if my_list[n_1]- my_list[n_0] ==1:
            n_0 += 1
            n_1 += 1
        
        

    return is_con 
# well prof my time ran out ;-;

print(are_all_consecutive([1,2,3]))
print(are_all_consecutive([7,8,9,10]))
print(are_all_consecutive([8]))
print(are_all_consecutive([1,2,2,3]))
print(are_all_consecutive([1,2,4,5]))