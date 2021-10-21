from numpy import log
def how_many_divide(number):
    counter = int((log(number)/log(2))) 
    if counter % 2 != 0:
        counter = counter -1 
    return counter
print(how_many_divide(3))
print(how_many_divide(4))
print(how_many_divide(12))
print(how_many_divide(64))