def is_prime(number):
    is_p = None
    if number > 1:
        for j in range(2,number):
            if number%j==0:
                is_p = False
                return is_p
        else:
            is_p = True
            return is_p
    else:
        is_p = False
        return is_p