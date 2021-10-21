def how_many_divide(number):
    counter = 0
    number_is_even = False
    if number % 2 == 0:
        number_is_even = True
    while number_is_even:
        number = number / 2
        counter += 1
        if number % 2 != 0:
            return counter
    return counter