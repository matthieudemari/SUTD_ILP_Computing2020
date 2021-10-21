def old_enough(age):
    can_vote = (age>=21)
    if (can_vote==True):
        number = None
    elif(can_vote==False):
        number=21-age
    return can_vote, number