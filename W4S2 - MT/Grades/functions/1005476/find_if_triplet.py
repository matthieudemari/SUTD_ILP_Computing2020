def are_all_consecutive(my_list):
    ordered_list = []
    first_number = my_list[0]
    for number in range(first_number, first_number + len(my_list) ):
        ordered_list.append(number)
    print(ordered_list)
    if ordered_list == my_list:
        is_cons = True
    else:
        is_cons = False
    return is_cons