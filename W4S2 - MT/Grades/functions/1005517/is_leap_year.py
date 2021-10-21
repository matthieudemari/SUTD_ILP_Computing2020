def old_enough(age):
    #strictly positive
    #at least 21
    if age >= 21:
        can_vote = True
        number = None

    #no. of years have to wait
 
    else:
        number = 21 - age
        can_vote = False
    return can_vote, number

