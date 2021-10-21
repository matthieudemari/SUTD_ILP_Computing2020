def old_enough(age):
    can_vote = None
    number = None
    check=True
    if(age>0):
        
        if(age>=21):
            can_vote=True
            number=None
            check=False
        else:
            can_vote=False
            number=(21-age)
            
    else:
        print("Age cannot be negative")
        
    return can_vote, number

print(old_enough(42))
print(old_enough(18))
print(old_enough(21))
