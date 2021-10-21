def find_if_triplet(my_list):
    has_triplet = True
    counter = 0
    a = my_list[0]
    for i in my_list:
        print(i)
        if my_list.count(i) >= 3:
            return True
    

print(find_if_triplet([1,1,1]))
print(find_if_triplet([1,2,3,3,3]))
print(find_if_triplet([1,2,2,2,2,3]))
print(find_if_triplet([1,2,2,3,4,4,5]))