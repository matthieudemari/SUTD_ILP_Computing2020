def are_all_consecutive(my_list):
    
    for index in range(len(my_list)):
        #print("values:", value)
        print("index:", index)
        print("value", my_list[index])
        
        if my_list[index] + 1 == my_list[index+1]:
            is_cons = True
        else:
            is_cons = False
    
    
    
    #is_cons = None
    return is_cons

print(are_all_consecutive([1,2,3]))
print(are_all_consecutive([7,8,9,10]))
print(are_all_consecutive([8]))
print(are_all_consecutive([1,2,2,3]))
print(are_all_consecutive([1,2,4,5]))