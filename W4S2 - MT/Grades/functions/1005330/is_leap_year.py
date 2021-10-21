def old_enough(age):
    if(age >= 21):
        can_vote = True
    else:
        can_vote = False
        
    if(can_vote == False):
        number = 21 - age
    else:
        number = None
    return can_vote, number