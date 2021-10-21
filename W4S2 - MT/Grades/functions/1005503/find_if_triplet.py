def find_if_triplet(my_list):
    empty_list = []
    has_triplet = None
    for index, value in enumerate(my_list):
        if value not in empty_list:
            empty_list.append(value)
            my_list.remove(value)
        if len(my_list)>=2:
            has_triplet = True
        else:
            has_triplet = False
        
    return has_triplet

print(find_if_triplet([1,1,1]))
print(find_if_triplet([1,2,3,3,3]))
print(find_if_triplet([1,2,2,2,2,3]))
print(find_if_triplet([1,2,2,3,4,4,5]))