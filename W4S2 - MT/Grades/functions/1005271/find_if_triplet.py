def are_all_consecutive(my_list):
    if (len(my_list)>1):
        for index, value in enumerate (my_list):
            while (index < len(my_list)):
                if (my_list[index+1]-my_list[index]==1):
                    is_cons= True
                else:
                    is_cons= False
    else:
        is_cons= True
    return is_cons

print(are_all_consecutive([1,2,3]))
print(are_all_consecutive([7,8,9,10]))
print(are_all_consecutive([8]))
print(are_all_consecutive([1,2,2,3]))
print(are_all_consecutive([1,2,4,5]))