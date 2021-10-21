def old_enough(age):
    if(age>=21):
        bool1=(age>=21)
        print(bool1)
        print("can vote=bool1")
        
    elif(age<21):
        bool2=(age<21)
        print("can_vote=bool2")
        
    return can_vote, number

print(old_enough(42))
print(old_enough(18))
print(old_enough(21))