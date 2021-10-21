def find_if_triplet(my_list):
    counter = 0
    for i in my_list:
        if i >= 1:
            counter += 1
            if counter >= 3:
                return True
        
    return counter

print(find_if_triplet([1,1,1]))
print(find_if_triplet([1,2,3,3,3]))
print(find_if_triplet([1,2,2,2,2,3]))
print(find_if_triplet([1,2,2,3,4,4,5]))