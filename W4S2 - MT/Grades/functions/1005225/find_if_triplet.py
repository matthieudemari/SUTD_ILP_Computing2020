def are_all_consecutive(my_list):
    is_cons = True
    number = my_list[0]
    for i in my_list[1:]:
        next_num_predict= number + 1 
        if next_num_predict != i:
            is_cons= False 
            break
        else: 
            number= i
    return is_cons
        

print(are_all_consecutive([1,2,3]))
print(are_all_consecutive([7,8,9,10]))
print(are_all_consecutive([8]))
print(are_all_consecutive([1,2,2,3]))
print(are_all_consecutive([1,2,4,5]))