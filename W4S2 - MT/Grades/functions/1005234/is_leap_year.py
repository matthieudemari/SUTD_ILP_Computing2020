def old_enough(age):
    can_vote = False
    if age<21:
        can_vote = False
        number = 21 - age
    elif age >= 21:   
        can_vote = True
        number = None
    return can_vote, number