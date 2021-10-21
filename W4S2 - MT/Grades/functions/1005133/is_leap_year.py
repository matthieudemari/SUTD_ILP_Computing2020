def old_enough(age):
    can_vote = age >= 21 # output is in boolean form
    if(can_vote): number = None
    else: number = 21 - age
    return can_vote, number