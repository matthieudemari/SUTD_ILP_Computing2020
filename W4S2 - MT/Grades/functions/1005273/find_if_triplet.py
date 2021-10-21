def are_all_consecutive(my_list):
    is_cons = False
    for index, number in enumerate(my_list):
        #print (index, number)
        if (index == (number - my_list[0])):
            is_cons = True
        else:
            is_cons = False
    return is_cons