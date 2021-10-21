def are_all_consecutive(my_list):
    is_cons=True
    
    for i in my_list:
        while (i < (len(my_list)-2)):
            if (my_list[i+1]== my_list[i]+1):
                is_cons = True
                
            else:
                is_cons = False
                break
        break
                
    return is_cons

print(are_all_consecutive([1,2,3]))
print(are_all_consecutive([7,8,9,10]))
print(are_all_consecutive([8]))
print(are_all_consecutive([1,2,2,3]))
print(are_all_consecutive([1,2,4,5]))