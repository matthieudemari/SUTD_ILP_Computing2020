def find_if_triplet(my_list):
    for i in my_list:
        if (my_list[i+1]):
            has_triplet = True
        else:
            has_triplet = False
    return has_triplet

print(find_if_triplet([1,1,1]))
print(find_if_triplet([1,2,3,3,3]))
print(find_if_triplet([1,2,2,2,2,3]))
print(find_if_triplet([1,2,2,3,4,4,5]))