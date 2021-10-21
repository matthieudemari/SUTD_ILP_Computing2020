def old_enough(age):
    can_vote = None
    number = None
    if age >= 21:
        can_vote = True
    else:
        can_vote = False
        number = 21 - age
    return can_vote, number

print(old_enough(42))
print(old_enough(18))
print(old_enough(21))