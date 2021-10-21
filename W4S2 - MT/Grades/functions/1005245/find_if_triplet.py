def are_all_consecutive(my_list):
    is_cons = None
    fe=my_list[0]
    counter=0
    for i in range(1,len(my_list)):
        if (my_list[i]==(fe+int(i))):
            counter+=1
        else:
            counter=counter
    if (counter==(len(my_list)-1)):
        is_cons=True
    else:
        is_cons=False
    return is_cons

print(are_all_consecutive([1,2,3]))
print(are_all_consecutive([7,8,9,10]))
print(are_all_consecutive([8]))
print(are_all_consecutive([1,2,2,3]))
print(are_all_consecutive([1,2,4,5]))