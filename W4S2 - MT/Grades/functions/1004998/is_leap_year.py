def old_enough(age):
    can_vote = None
    number = None
    if age >= 21:
        can_vote = True
    elif age < 21:
        can_vote = False
        number = 21 - age
    return print("can_vote = {}" .format(can_vote)), print("number = {}" .format(number))

print(old_enough(42))
print(old_enough(18))
print(old_enough(21))