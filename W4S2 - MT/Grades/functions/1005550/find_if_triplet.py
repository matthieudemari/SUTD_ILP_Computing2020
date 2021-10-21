def find_if_triplet(my_list):
    
    for elements in my_list:
        if my_list.count(elements) >= 3:
            return True
    
    return False

print(find_if_triplet([1,1,1]))
print(find_if_triplet([1,2,3,3,3]))
print(find_if_triplet([1,2,2,2,2,3]))
print(find_if_triplet([1,2,2,3,4,4,5]))