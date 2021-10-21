def find_if_triplet(my_list):
    has_triplet = False
  
    for i in my_list:
        a = my_list.count(i)
        print(a)
        if(a >= 3):
            return True
        else: 
            return False
    return has_triplet