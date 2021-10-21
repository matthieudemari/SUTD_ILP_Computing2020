def old_enough(age):
    # Bool for whether you can vote
    can_vote = (age >= 21)
    # If the person is under age, returns the years left to 21
    number = int(age < 21)*(21-age)
    # Since question asks for "None" if can_vote, change number to None
    if (can_vote):
        number = None
    return can_vote, number