def are_all_consecutive(my_list):
    is_cons = True
    if len(my_list) == 1:
        is_cons = True
    elif len(my_list) > 1:
        for index, val in enumerate(my_list):
            num1 = val
            num2 = my_list[index +1]
            for i in range(my_list):
                if num2 - num1 == 1:
                    is_cons = True
                else:
                    is_cons = False
    return is_cons
