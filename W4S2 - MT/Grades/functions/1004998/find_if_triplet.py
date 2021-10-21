def are_all_consecutive(my_list):
    print(my_list)
    is_cons = None
    newlist = []
    for i, number in enumerate(my_list):
        newlist.append(my_list[-1] - (i))
    print(newlist[::-1])
    if newlist[::-1] == my_list:
        is_cons = True
    else:
        is_cons = False
    
            
    return is_cons

print(are_all_consecutive([1,2,3]))
print(are_all_consecutive([7,8,9,10]))
print(are_all_consecutive([8]))
print(are_all_consecutive([1,2,2,3]))
print(are_all_consecutive([1,2,4,5]))