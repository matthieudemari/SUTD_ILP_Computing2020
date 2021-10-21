def how_many_divide(number):
    if number == 0:
        return "infinity"
    count = 0
    while (number % 2 == 0):
        number = int(number / 2)
        count += 1
    return count