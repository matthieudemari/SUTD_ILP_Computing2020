def old_enough(age):
    can_vote = True
    number = 0
    if (age < 0):
        print("Your age cannot be less than 0. Please key in your age again.")
    elif (age >= 21):
        can_vote = True
        number = None
    elif (age < 21):
        can_vote = False
        number = 21 - age
    return can_vote, number