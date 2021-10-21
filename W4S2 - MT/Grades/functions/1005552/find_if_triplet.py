def are_all_consecutive(my_list):
    is_cons = False
    list1 = [my_list[0]]
    if len(my_list) == 1:
            is_cons = True
    for index, element in enumerate(my_list):
        diff = my_list[index] - my_list[index-1]
        if diff == 1:
                list1.append(element)
    if my_list == list1:
        is_cons = True                
    return is_cons