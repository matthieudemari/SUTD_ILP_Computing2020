def old_enough(age):
    if age < 21:
        can_vote = False
        number = 21 - age
        
    else:
        can_vote = True
        number = None
        
    return can_vote, number

print(old_enough(42))
print(old_enough(18))
print(old_enough(21))