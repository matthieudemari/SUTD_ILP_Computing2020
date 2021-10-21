def find_if_triplet(my_list):
    counter = []
    
    for i in my_list:
        if i not in counter:
            counter.append(i)
    diff_in_value = len(my_list) - len(counter)
    
    if diff_in_value >= 2:
        has_triplet = True
    else:
        has_triplet = False
    return has_triplet

print(find_if_triplet([1,1,1]))
print(find_if_triplet([1,2,3,3,3]))
print(find_if_triplet([1,2,2,2,2,3]))
print(find_if_triplet([1,2,2,3,4,4,5]))