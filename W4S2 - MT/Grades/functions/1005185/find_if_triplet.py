def find_if_triplet(my_list):
    
    x=0
    count=0
    bool1=False
    
    for index,i in enumerate(my_list):
        
        if(index< len(my_list)-1):
             if(my_list[index-1]== my_list[index] and my_list[index]== my_list[index+1] ):
                bool1=True
                break      
        
    has_triplet = bool1
    return has_triplet
