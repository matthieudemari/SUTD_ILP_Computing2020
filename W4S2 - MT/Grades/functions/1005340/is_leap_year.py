def old_enough(age):
    can_vote = bool1 = (age >= 21)
    
    number = 21 - age
    
    if(age >= 21) :
        print(None)

    elif (age < 21) :
        print(number)
        
    return can_vote, number

print(old_enough(42))
print(old_enough(18))
print(old_enough(21))