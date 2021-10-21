def how_many_months(initial_amount, rate):
    additional_amount_at_end_of_month= int((initial_amount*(1+(rate/10))**2)-initial_amount)
    months= 1000000/int(additional_amount_at_end_of_month)
    return months

print(how_many_months(10000, 1.0))
print(how_many_months(10000, 5.0))
print(how_many_months(100000, 5.0))
print(how_many_months(1000000, 5.0))