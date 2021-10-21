def are_all_consecutive(my_list):
    list_store = []
    
    for index, elem in enumerate(my_list):
        # To fix the [index - 1]
        if (index == 0):
            list_store.append(elem)
        # Appends the element if the diff between current val and val before is 1
        if (elem - (my_list[index - 1]) == 1):
            list_store.append(elem)
    
    # If both list_store and my_list are the same, it is consecutive
    is_cons = (list_store == my_list)
    return is_cons