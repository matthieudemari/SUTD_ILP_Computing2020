def how_many_months(initial_amount, rate):
	account = initial_amount
	months = 0
	while(account < 1000000):
		account = account * (1 + (rate/100))
		months += 1
	return months