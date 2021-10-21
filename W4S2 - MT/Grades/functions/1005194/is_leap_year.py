def old_enough(age):
    age_number = int(age)
    can_vote = bool(age_number>=21)
    if (age_number>=21):
        number = None
    else:
        number = 21 - age_number
    return can_vote, number

print(old_enough(42))
print(old_enough(18))
print(old_enough(21))

Answers:
(True, None)
(False, 3)
(True, None)