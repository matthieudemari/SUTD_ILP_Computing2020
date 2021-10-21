def find_if_triplet(my_list):
    for number in my_list:
        repetition= my_list.count(number)
        has_triplet== False
        if repetition>=3:
            has_triplet== True
        else:
            has_triplet== False
    return has_triplet