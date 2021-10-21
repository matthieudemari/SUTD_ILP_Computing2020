def are_all_consecutive(my_list):
    if len(my_list) > 1:
        for index, num in enumerate(my_list):
            length = len(my_list) - 1
            for index in range(0, length):
                    if my_list[index + 1] - my_list[index] == 1:
                        is_cons = True
                    else:
                        # the moment the different between two adjacent elements is not 1, the list is not consecutive
                        is_cons = False
                        
                        # end loop
                        break
    else:
        is_cons = True
    
    return is_cons

print(are_all_consecutive([1,2,3]))
print(are_all_consecutive([7,8,9,10]))
print(are_all_consecutive([8]))
print(are_all_consecutive([1,2,2,3]))
print(are_all_consecutive([1,2,4,5]))