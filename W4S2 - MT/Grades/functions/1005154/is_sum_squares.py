def is_prime(number):
	if number == 1:
		is_p = True
		return is_p
	else:
		dividing = 1
		divisors = []
		while(dividing <= number):
			if number % dividing == 0:
				divisors.append(number/dividing)
			dividing += 1
		if divisors == [number, 1]:
			is_p = True
		else:
			is_p = False
		return is_p