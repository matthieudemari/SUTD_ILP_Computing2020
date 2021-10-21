def old_enough(age):
    can_vote = age >= 20
    number = None
    if(age <= 20 and age >= 0):
        number = 21 - age 
        print("{} more year(s) to vote".format(number))
    elif(age == 0 or age <= 0):
        number = "Invalid Age"
    else:
        number = None
    
    return can_vote, number


print(old_enough(42))
print(old_enough(18))
print(old_enough(10))
print(old_enough(-10))
print(old_enough(21))
