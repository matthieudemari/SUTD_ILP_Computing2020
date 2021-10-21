def is_sum_squares(number):
    list1 = [0,1,2,3,4,5]
    list2 = []
    for a in list1:
        list2.append(a**2)
        print (list2)
    for b in list2:
        if (number - b)**0.5 is int:
            return True
        else:
            return False


print(is_sum_squares(9))
print(is_sum_squares(5))
print(is_sum_squares(50))
print(is_sum_squares(7))