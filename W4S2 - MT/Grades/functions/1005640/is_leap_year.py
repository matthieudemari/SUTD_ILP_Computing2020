def old_enough(age):
    
    can_vote = False
    if age >= 21:
        can_vote = True
    
    number = None
    if not can_vote:
        number = 21 - age
    return can_vote, number

print(old_enough(42))
print(old_enough(18))
print(old_enough(21))