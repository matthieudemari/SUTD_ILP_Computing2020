from numpy import(log)

def how_many_months(initial_amount, rate):
    new_amount = initial_amount
    while new_amount<1000000:
        new_amount += initial_amount*(rate/100)
    #After n number of months, new_amount = initial_amount*(1+rate/100)**n
    #log(new_amount) = log(initial_amount) +n(log(1+rate/100))
    n= (log(new_amount)-log(initial_amount)) / (log(1+rate/100))
    if n==0:
        months= 0
    else:
        months= int(n)+1
    return months

print(how_many_months(10000, 1.0))
print(how_many_months(10000, 5.0))
print(how_many_months(100000, 5.0))
print(how_many_months(1000000, 5.0))