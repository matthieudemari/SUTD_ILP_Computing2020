def is_sum_squares(number):
    is_sq = True
    a=[0,1,2,3,4,5,6,7,8,9,10]
    b=[0,1,2,3,4,5,6,7,8,9,10]
  
    for i in a:
        for i in b:
            total=a**2+b**2
            if number == total:
                return ("is_sq={}".format(is_sq))
            else:
                return ("is_sq={}".format(not is_sq))
