def find_if_triplet(my_list):
    has_triplet = True
    counter_list=[]
    for i in my_list:
        counter=int(my_list.count(i))
        counter_list.append(counter)
        if max(counter_list)>2:
            has_triplet=True
        elif counter<3:
            has_triplet=False
    return has_triplet