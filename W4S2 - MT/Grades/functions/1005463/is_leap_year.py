def old_enough(age):
    can_vote = True 
    number = 21 - age
    
    if(age >= 21):
        number = None 
        print(can_vote, number)
    else:
        print(not can_vote, number)
    
    return can_vote, number