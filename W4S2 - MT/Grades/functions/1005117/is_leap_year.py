def old_enough(age):
    voting_age = 21
    can_vote = age >= voting_age
    number = None if can_vote else (voting_age - age)
    return can_vote, number