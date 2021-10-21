def find_if_triplet(my_list):
    def has_triplet(n):
        if my_list[n]==my_list[n+1]==my_list[n+2]:
            return True
        elif my_list[n] != my_list[n+1]:
            i=+1
            return
        else:
            return False

print(find_if_triplet([1,1,1]))
print(find_if_triplet([1,2,3,3,3]))
print(find_if_triplet([1,2,2,2,2,3]))
print(find_if_triplet([1,2,2,3,4,4,5]))