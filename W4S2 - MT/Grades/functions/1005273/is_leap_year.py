def old_enough(age):
    can_vote = False
    number = None
    
    #check if old enough
    if (age >= 21):
        can_vote = True
    elif (0 < age < 21):
        age_difference = 21-age
        number = age_difference  
    elif (age<0):
        print ("Age cannot be negative")
    return can_vote, number
