from numpy import log

def how_many_divide(number):
    counter = 0
    if number%3:
      counter = log(number/3) / log(2)
    return counter
    else:
      counter = log(number)/log(2)
    return counter

print(how_many_divide(3))
print(how_many_divide(4))
print(how_many_divide(12))
print(how_many_divide(64))