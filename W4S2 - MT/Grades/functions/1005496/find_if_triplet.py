def find_if_triplet(my_list):
    match = 0
    counter = 0
    counter2 = 0
    total = len(my_list)
    for i in my_list:
        counter += 1
        counter2 = 0
        match = 0;
        while((counter+counter2) < total):
            if(my_list[counter + counter2] == i):
                match += 1
            counter2 += 1
        if(match >= 2):
            return True
    return False


print(find_if_triplet([1,1,1]))
print(find_if_triplet([1,2,3,3,3]))
print(find_if_triplet([1,2,2,2,2,3]))
print(find_if_triplet([1,2,2,3,4,4,5]))