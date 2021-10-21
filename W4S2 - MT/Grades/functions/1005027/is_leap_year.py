def old_enough(age):
    can_vote = False
    number = None
    if(age >= 21):
        can_vote = True
    else:
        number = 21 - age        
        
    return can_vote, number