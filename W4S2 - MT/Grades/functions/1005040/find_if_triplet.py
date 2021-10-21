def find_if_triplet(my_list):
    new_list = []
    triplet_list= []
    has_triplet = None
    for list in my_list:
        if(list not in new_list):
            new_list.append(list)
        elif(list in new_list):
            triplet_list.append(list)
    if(len(triplet_list) > 2 or  = 2):
        has_triplet = True
        return has_triplet