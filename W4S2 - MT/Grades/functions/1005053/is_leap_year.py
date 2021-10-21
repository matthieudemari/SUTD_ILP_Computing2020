def old_enough(age):
    can_vote = (age >= 21)
    if(age < 21):
        number = 21 - age
    else:
        number = None
    return can_vote, number

print(old_enough(42))
print(old_enough(18))
print(old_enough(21))