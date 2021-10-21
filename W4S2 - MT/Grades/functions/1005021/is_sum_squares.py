def is_sum_squares(number):
    is_sq = False
    for i in range(number):
      for j in range(number):
        if(i**2 + j**2) == number:
          is_sq = True
          break
    return is_sq