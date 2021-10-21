def old_enough(age):
    can_vote = age
    boolean1 = can_vote >= 21
    if boolean1:
        print(boolean1)
        number = None
    else:
        print(boolean1)
        number = 21 - age
    return can_vote, number