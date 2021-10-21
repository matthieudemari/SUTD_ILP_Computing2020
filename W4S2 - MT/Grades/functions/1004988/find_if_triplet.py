def find_if_triplet(my_list):
    counter = 0
    for i in my_list:
#        print("i:", i)
        for j in my_list:
#            print("j:", j)
            if(i == j):
                counter += 1
#            print("counter:", counter)
            if(counter>2):
                return True
        counter = 0
    return False