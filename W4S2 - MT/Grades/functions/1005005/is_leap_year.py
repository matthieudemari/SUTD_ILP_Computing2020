def old_enough(age):
    vote_bool = age >= 21
    if (vote_bool):
        can_vote = vote_bool
        number = None
        
    elif (not vote_bool):
        can_vote = False
        number = 21 - age
        
    print ("can_vote = {} and number = {}".format (can_vote, number))