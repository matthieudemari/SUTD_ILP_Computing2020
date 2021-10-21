
def are_all_consecutive(my_list):
    is_cons = None
    total = 0
    minimum = min(my_list)
    maximum = max(my_list)

    newlist = []

    for n in my_list:
        if n in newlist:
            is_cons = False
            return is_cons

        newlist.append(n)

        if n < minimum:
            minimum = n

        if n > maximum:
            maximum = n

        total += n

    if (2 * total != maximum * (maximum + 1) - minimum * (minimum - 1)):
        is_cons = False
        return is_cons
    else:
        is_cons = True
    return is_cons
    