def old_enough(age):
    number = 0
    if (age >= 21):
        can_vote = True
    else:
        can_vote = False
    
    if (can_vote == True):
        number = None
    elif (can_vote == False):
        number = 21 - age
    return can_vote, number