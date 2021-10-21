#also tried my best, sorry again
def find_if_triplet(my_list):
    has_triplet = None
    counter = 0
    for index ,i in enumerate (my_list):
        if my_list[index] == my_list[index + 1]:
            counter += 1
    if counter >= 3:
        has_triplet = True
        
    else:
        has_triplet = False
        
    return has_triplet