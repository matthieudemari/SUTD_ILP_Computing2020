def find_if_triplet(my_list):
    i = 0
    x = 0
    while i < 3:
        if my_list[x] == my_list[x+1]:
            i += 1
        else:
            x += 1
  