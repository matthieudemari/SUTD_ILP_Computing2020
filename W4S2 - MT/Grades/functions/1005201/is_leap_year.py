def old_enough(age):
    can_vote = None
    number = None
    if(age >= 21):
        can_vote = True
        number = 0
    elif(age < 21):
        can_vote = False
        number = 21-age
    return can_vote, number