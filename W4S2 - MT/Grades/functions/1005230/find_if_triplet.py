def find_if_triplet(my_list):
    has_triplet=True
    
    for index in my_list:
        counting=my_list.count(my_list[index])
        print(counting)
        if counting >=3:
            has_triplet
        else:
            has_triplet=False
           
    return has_triplet

print(find_if_triplet([1,1,1]))
print(find_if_triplet([1,2,3,3,3]))
print(find_if_triplet([1,2,2,2,2,3]))
print(find_if_triplet([1,2,2,3,4,4,5]))