def find_if_triplet(my_list):
    counter=0
    single_list=[]
    second_list=[]
    third_list=[]
    for a in my_list:
        if(a not in single_list):
            single_list.append(a)
            my_list.remove(a)
    for a in my_list:
        for b in single_list:
            if(a not in second_list):
                second_list.append(a)
                my_list.remove(a)
    for a in my_list: 
        for c in third_list:
            if(a not in third_list):
                third_list.append(a)
    if(third_list!=[]):
        has_triplet=True
    elif(third_list==[]):
        has_triplet==False        
    return has_triplet