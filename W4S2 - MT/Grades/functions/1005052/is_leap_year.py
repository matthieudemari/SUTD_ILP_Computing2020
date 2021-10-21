def old_enough(age):
    if(age >= 21):
        can_vote = True
        number = None
    elif(age < 21):
        can_vote = False
        number = 21 - age
    return can_vote, number