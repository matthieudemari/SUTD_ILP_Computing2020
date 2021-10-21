def old_enough(age):
    can_vote = (age>=21)
    number = None
    if(not can_vote):
        number = 21 - age
    return can_vote, number