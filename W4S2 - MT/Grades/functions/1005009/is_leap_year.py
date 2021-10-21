def old_enough(age):
    #set can vote age to 21 and up
    can_vote = age >= 21
    #if cannot vote
    if not can_vote:
        #number = 21 - current age
        number = 21 - age
    #if can vote
    else:
        #return none
        number = None
    return can_vote, number