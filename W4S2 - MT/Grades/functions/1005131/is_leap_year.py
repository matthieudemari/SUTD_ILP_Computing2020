def old_enough(age):
    if(age>=21):
        can_vote = True
    else:
        can_vote = False
    if(age<21):
        number = 21 - int(age)
    else:
        number=None
    return can_vote, number