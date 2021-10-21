def how_many_divide(number):
  count = 0
  while(number%2 == 0 and number !=0):
    number = number/2
    count +=1
  return count