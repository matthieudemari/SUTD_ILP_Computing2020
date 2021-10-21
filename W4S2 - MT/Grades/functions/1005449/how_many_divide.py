def how_many_months(initial_amount, rate):
    months = 0
    difference = 1000000- initial_amount
    n=0
    while difference > 0:
        n=n+1
        difference=1000000- initial_amount*(1+(rate/100))**(n)
    months = months+n
    return months

print(how_many_months(10000, 1.0))
print(how_many_months(10000, 5.0))
print(how_many_months(100000, 5.0))
print(how_many_months(1000000, 5.0))