def find_if_triplet(my_list):
    count=1
    has_triplet=False
    for index,value in enumerate(my_list):
        if index==len(my_list)-1:
            break
        if my_list[index]==my_list[index+1]:
            count+=1
            if count==3:
                has_triplet=True
                break
        else:
            count=1
    return has_triplet