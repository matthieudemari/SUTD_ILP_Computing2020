def find_if_triplet(my_list):
    bool1 = True
    has_triplet = len(set(my_list))==bool1
    return has_triplet

print(find_if_triplet([1,1,1]))
print(find_if_triplet([1,2,3,3,3]))
print(find_if_triplet([1,2,2,2,2,3]))
print(find_if_triplet([1,2,2,3,4,4,5]))