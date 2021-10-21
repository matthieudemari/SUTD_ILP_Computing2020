def old_enough(age):
    can_vote = bool(int(age)>=21)
    number=0
    if age<21:
        number=21-int(age)
    else:
        number = None
    return can_vote, number

print(old_enough(42))
print(old_enough(18))
print(old_enough(21))