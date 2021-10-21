def old_enough(age):
    
    if (age>=21):
        can_vote = True
        number = None
        return can_vote, number
    else:
        can_vote = False
        number = 21 - age
        #print("number:",number)
        return can_vote, number
    
    
    #return can_vote, number

print(old_enough(42))
print(old_enough(18))
print(old_enough(21))