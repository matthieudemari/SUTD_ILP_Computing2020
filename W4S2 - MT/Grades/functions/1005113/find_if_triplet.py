def find_if_triplet(my_list):
    for i in my_list:
        count = 0
        for j in my_list:
            if i == j:
                count += 1          
        if count >= 3:
            return True
    return  False   
          

print(find_if_triplet([1,1,1]))
print(find_if_triplet([1,2,3,3,3]))
print(find_if_triplet([1,2,2,2,2,3]))
print(find_if_triplet([1,2,2,3,4,4,5]))