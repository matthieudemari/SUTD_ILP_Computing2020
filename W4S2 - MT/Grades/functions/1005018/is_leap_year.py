def old_enough(age):
    #checking if person is above 21 
    can_vote = (age >= 21)
    #checking the number of years needed for him to start voting 
    if (age >= 21):
        number = None
    #for those below 21 
    elif (age < 21):
    # number of years needed
        number = 21 - age
        
    return can_vote, number

print(old_enough(42))
print(old_enough(18))
print(old_enough(21))