def are_all_consecutive(my_list):
	initial = my_list[0]
	is_cons = True
	for x in my_list:
		if x == initial:
			initial += 1
			continue
		else:
			is_cons = False
			break
	return is_cons