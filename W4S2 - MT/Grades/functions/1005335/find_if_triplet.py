def are_all_consecutive(my_list):
    if len(my_list)==1:
        is_cons=True
    else:
        for i,v in enumerate(my_list):
            if i+1 <=(len(my_list)-1):
                if v+1==my_list[i+1]:
                    is_cons=True
                else:
                    is_cons=False
                    break
    return is_cons