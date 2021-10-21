def find_if_triplet(my_list):
    counter = 0
    has_triplet = False
    for i1 in my_list:
        if my_list.count(i1)>=3:
            has_triplet = True
    return has_triplet

print(find_if_triplet([1,1,1]))
print(find_if_triplet([1,2,3,3,3]))
print(find_if_triplet([1,2,2,2,2,3]))
print(find_if_triplet([1,2,2,3,4,4,5]))