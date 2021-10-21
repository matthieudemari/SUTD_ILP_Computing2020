def old_enough(age):
    can_vote = (age >= 21)
    number = (21 - age)    
    if number <= 0:
        number = None
    return can_vote, number

print(old_enough(42))
print(old_enough(18))
print(old_enough(21))