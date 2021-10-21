def are_all_consecutive(my_list):
    sort_list = sorted(my_list)
    for i in range(len(my_list)):
        for val in range(len(my_list)):
            if my_list[i] ==  sort_list[val]:
                is_cons = True
            else:
                is_cons = False
    return is_cons

print(are_all_consecutive([1,2,3]))
print(are_all_consecutive([7,8,9,10]))
print(are_all_consecutive([8]))
print(are_all_consecutive([1,2,2,3]))
print(are_all_consecutive([1,2,4,5]))