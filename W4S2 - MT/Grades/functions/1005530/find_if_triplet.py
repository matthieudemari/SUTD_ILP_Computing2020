def find_if_triplet(my_list):
    has_triplet = False
    new_list=[]
    for i in my_list:
        if (i not in new_list):
            new_list.append(i)
    if (len(my_list)-len(new_list))%2==0:
        return not has_triplet
    else:
        return has_triplet

print(find_if_triplet([1,1,1]))
print(find_if_triplet([1,2,3,3,3]))
print(find_if_triplet([1,2,2,2,2,3]))
print(find_if_triplet([1,2,2,3,4,4,5]))