def find_if_triplet(my_list):
  has_triplet = False
  for i in my_list:
    counter =0
    for j in my_list:
      if i ==j:
        counter +=1
        if counter >=3:
          has_triplet = True
          break
  return has_triplet