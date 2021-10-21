def are_all_consecutive(my_list):
    is_cons = False
    check_list = []
    number = my_list[0]
    while(len(check_list) < len(my_list)):
        check_list.append(number)
        number += 1
    if(my_list == check_list):
        is_cons = True
    
    return is_cons